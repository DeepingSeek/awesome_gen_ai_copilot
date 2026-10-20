#!/usr/bin/env python3
"""Track upstream projects listed in README.md, record changes, and refresh README metadata. Stdlib only."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

API = "https://api.github.com"
REPO_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
LINE_RE = re.compile(r"^(- \[[^\]]*\]\((https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\)\s-\s.*?)(\s<sub>.*?</sub>)?$")
BOARD_BEGIN = "<!-- BEGIN:recent-updates -->"
BOARD_END = "<!-- END:recent-updates -->"
# GitHub site pages that match the URL shape but are not projects.
NON_PROJECT_OWNERS = {
    "about", "collections", "customer-stories", "events", "explore", "features",
    "login", "marketplace", "notifications", "orgs", "readme", "settings", "signup",
    "sponsors", "topics", "user-attachments", "apps", "security", "pricing", "trending",
}
STALE_DAYS = 365
RECENT_DAYS = 7
BOARD_SIZE = 10
MAX_SUMMARY = 80
MIN_REPOS = 50          # guard: a README parse below this means something is wrong
MAX_UNKNOWN_RATIO = 0.3  # guard: too many failed lookups means likely rate limiting


def parse_repos(text: str) -> list[tuple[str, str]]:
    seen: dict[str, tuple[str, str]] = {}
    for owner, name in REPO_RE.findall(text):
        name = name.removesuffix(".git")
        if owner.lower() in NON_PROJECT_OWNERS:
            continue
        seen.setdefault(f"{owner}/{name}".lower(), (owner, name))
    return sorted(seen.values(), key=lambda p: f"{p[0]}/{p[1]}".lower())


def api_get(path: str, token: str | None) -> tuple[int, Any]:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(API + path, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, None
    except (urllib.error.URLError, TimeoutError):
        return -1, None


def clip(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(text.split()))
    text = re.sub(r"[`*_#]", "", text).strip()
    return text if len(text) <= MAX_SUMMARY else text[: MAX_SUMMARY - 1] + "…"


def release_summary(body: str | None) -> str:
    for block in re.split(r"\n\s*\n", body or ""):
        if block.strip() and not block.lstrip().startswith("#"):
            return clip(block)
    return ""


def commit_summary(messages: list[str]) -> str:
    heads = [m.splitlines()[0] for m in messages if m.strip()]
    return clip("；".join(heads[:3])) or "仓库有新推送"


def fetch_commit_messages(repo: str, since: str, token: str | None) -> list[str]:
    code, commits = api_get(f"/repos/{repo}/commits?since={since}&per_page=3", token)
    if code != 200 or not isinstance(commits, list):
        return []
    return [c["commit"]["message"] for c in commits]


def build_entry(owner: str, name: str, token: str | None, now: datetime, previous: dict | None) -> dict:
    entry = {
        "repo": f"{owner}/{name}",
        "url": f"https://github.com/{owner}/{name}",
        "status": "unknown",
        "current_name": None,
        "stars": None,
        "pushed_at": None,
        "archived": None,
        "license": None,
        "latest_release": None,
        "tracked_update": (previous or {}).get("tracked_update"),
        "update_type": (previous or {}).get("update_type"),
        "update_summary": (previous or {}).get("update_summary", ""),
        "flags": [],
    }
    code, body = api_get(f"/repos/{owner}/{name}", token)
    if code == 404:
        entry["status"] = "missing"
        entry["flags"].append("missing")
        return entry
    if code != 200 or body is None:
        return entry

    current = body["full_name"]
    entry["status"] = "ok" if current.lower() == f"{owner}/{name}".lower() else "renamed"
    entry["current_name"] = current
    entry["stars"] = body.get("stargazers_count")
    entry["pushed_at"] = body.get("pushed_at")
    entry["archived"] = bool(body.get("archived"))
    entry["license"] = (body.get("license") or {}).get("spdx_id")

    # First run has no snapshot: pushed_at becomes the baseline and emits no change event.
    candidates: list[tuple[str, str, str]] = []
    previous_pushed = (previous or {}).get("pushed_at")
    if previous_pushed and entry["pushed_at"] != previous_pushed:
        messages = fetch_commit_messages(current, previous_pushed, token)
        candidates.append((entry["pushed_at"], "commit", commit_summary(messages)))

    release_code, release = api_get(f"/repos/{current}/releases/latest", token)
    if release_code == 200 and release:
        entry["latest_release"] = release.get("tag_name")
        previous_tag = (previous or {}).get("latest_release")
        if previous is not None and previous_tag != entry["latest_release"]:
            published = release.get("published_at") or entry["pushed_at"]
            candidates.append((published, "release", release_summary(release.get("body"))))

    if candidates:
        when, kind, summary = max(candidates, key=lambda c: c[0])
        entry.update(tracked_update=when, update_type=kind, update_summary=summary)

    if entry["status"] == "renamed":
        entry["flags"].append("renamed")
    if entry["archived"]:
        entry["flags"].append("archived")
    if entry["pushed_at"]:
        pushed = datetime.fromisoformat(entry["pushed_at"].replace("Z", "+00:00"))
        if pushed < now - timedelta(days=STALE_DAYS):
            entry["flags"].append("stale")
    return entry


def render_board(projects: list[dict], now: datetime) -> str:
    cutoff = now - timedelta(days=RECENT_DAYS)
    recent = [
        p for p in projects
        if p["tracked_update"]
        and datetime.fromisoformat(p["tracked_update"].replace("Z", "+00:00")) >= cutoff
    ]
    recent.sort(key=lambda p: p["tracked_update"], reverse=True)
    if not recent:
        return f"_近 {RECENT_DAYS} 天暂无更新。_"
    lines = []
    for index, project in enumerate(recent[:BOARD_SIZE], 1):
        kind = "Release" if project["update_type"] == "release" else "commit"
        lines.append(
            f"{index}. [{project['repo']}]({project['url']}) "
            f"<sub>{project['tracked_update'][:10]} · {kind}<br>{project['update_summary']}</sub>"
        )
    return "\n".join(lines)


def decorate_line(line: str, index: dict[str, dict]) -> str:
    match = LINE_RE.match(line)
    if not match:
        return line
    head, url = match.group(1), match.group(2)
    owner, name = REPO_RE.search(url).groups()
    project = index.get(f"{owner}/{name}".lower())
    if project is None or project["status"] == "unknown":
        return line
    if project["status"] == "missing":
        return f"{head} <sub>已失效</sub>"
    badges = []
    if project["pushed_at"]:
        badges.append(f"更新 {project['pushed_at'][:10]}")
    if project["stars"] is not None:
        badges.append(f"★ {project['stars']}")
    if project["license"]:
        badges.append(project["license"])
    if project["archived"]:
        badges.append("已归档")
    return f"{head} <sub>{' · '.join(badges)}</sub>" if badges else head


def apply_readme(text: str, projects: list[dict], board: str) -> str | None:
    if BOARD_BEGIN not in text or BOARD_END not in text:
        return None
    index = {p["repo"].lower(): p for p in projects}
    decorated = "\n".join(decorate_line(line, index) for line in text.split("\n"))
    pattern = re.compile(re.escape(BOARD_BEGIN) + r".*?" + re.escape(BOARD_END), re.S)
    return pattern.sub(lambda _: f"{BOARD_BEGIN}\n{board}\n{BOARD_END}", decorated, count=1)


def strip_stars(projects: list[dict]) -> list[dict]:
    return [{k: v for k, v in p.items() if k != "stars"} for p in projects]


def extract_board(text: str) -> str | None:
    match = re.search(re.escape(BOARD_BEGIN) + r"\n(.*?)\n" + re.escape(BOARD_END), text, re.S)
    return match.group(1) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="parse README only, no API calls")
    parser.add_argument("--limit", type=int, default=0, help="query at most N repos (testing)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    repos = parse_repos(readme)
    print(f"parsed {len(repos)} project repositories from README.md")

    if args.dry_run:
        return 0
    if not args.limit and len(repos) < MIN_REPOS:
        print(f"abort: fewer than {MIN_REPOS} repositories parsed", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN") or None
    now = datetime.now(timezone.utc)
    data_path = root / "data" / "upstream-status.json"
    previous_data = json.loads(data_path.read_text(encoding="utf-8")) if data_path.exists() else {}
    previous_by_repo = {p["repo"].lower(): p for p in previous_data.get("projects", [])}
    selected = repos[: args.limit] if args.limit else repos
    projects = [
        build_entry(owner, name, token, now, previous_by_repo.get(f"{owner}/{name}".lower()))
        for owner, name in selected
    ]
    projects.sort(key=lambda p: p["repo"].lower())

    unknown = sum(1 for p in projects if p["status"] == "unknown")
    if not args.limit and unknown / len(projects) > MAX_UNKNOWN_RATIO:
        print(f"abort: {unknown}/{len(projects)} lookups failed, not writing", file=sys.stderr)
        return 1

    summary = {
        "total": len(projects),
        "ok": sum(1 for p in projects if p["status"] == "ok"),
        "flagged": sum(1 for p in projects if p["flags"]),
        "unknown": unknown,
    }
    if args.limit:
        print(f"limited run, not writing: {summary}")
        return 0

    new_readme = apply_readme(readme, projects, render_board(projects, now))
    if new_readme is None:
        print(f"abort: README is missing {BOARD_BEGIN} / {BOARD_END} markers", file=sys.stderr)
        return 1
    board = render_board(projects, now)
    new_readme = apply_readme(readme, projects, board)
    if new_readme is None:
        print(f"abort: README is missing {BOARD_BEGIN} / {BOARD_END} markers", file=sys.stderr)
        return 1
    previous_projects = previous_data.get("projects")
    if previous_projects is not None and strip_stars(previous_projects) == strip_stars(projects) and extract_board(readme) == board:
        print("only stars changed, skipping commit")
        return 0

    data = {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": summary,
        "projects": projects,
    }
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"updated: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
