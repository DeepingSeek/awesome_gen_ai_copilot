#!/usr/bin/env python3
"""Refresh upstream status for projects listed in README.md. Stdlib only."""
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

API = "https://api.github.com"
REPO_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
# GitHub site pages that match the URL shape but are not projects.
NON_PROJECT_OWNERS = {
    "about", "collections", "customer-stories", "events", "explore", "features",
    "login", "marketplace", "notifications", "orgs", "readme", "settings", "signup",
    "sponsors", "topics", "user-attachments", "apps", "security", "pricing", "trending",
}
STALE_DAYS = 365
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


def api_get(path: str, token: str | None) -> tuple[int, dict | None]:
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


def build_entry(owner: str, name: str, token: str | None, now: datetime) -> dict:
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

    release_code, release = api_get(f"/repos/{current}/releases/latest", token)
    if release_code == 200 and release:
        entry["latest_release"] = release.get("tag_name")

    if entry["status"] == "renamed":
        entry["flags"].append("renamed")
    if entry["archived"]:
        entry["flags"].append("archived")
    if entry["pushed_at"]:
        pushed = datetime.fromisoformat(entry["pushed_at"].replace("Z", "+00:00"))
        if pushed < now - timedelta(days=STALE_DAYS):
            entry["flags"].append("stale")
    return entry


def render_markdown(data: dict) -> str:
    summary = data["summary"]
    lines = [
        "# 上游项目状态",
        "",
        "> 自动生成，请勿手动编辑。数据来源于 GitHub API，由 `scripts/track_upstream.py` 更新。",
        "",
        f"- 生成时间：{data['generated_at']}",
        f"- 项目总数：{summary['total']}，正常：{summary['ok']}，已标记：{summary['flagged']}，无法查询：{summary['unknown']}",
        "",
        "| 项目 | Stars | 最近推送 | 最新 Release | 许可证 | 标记 |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for project in data["projects"]:
        pushed = (project["pushed_at"] or "")[:10]
        flags = ", ".join(project["flags"]) or "-"
        stars = project["stars"] if project["stars"] is not None else "-"
        lines.append(
            f"| [{project['repo']}]({project['url']}) | {stars} | {pushed or '-'} | "
            f"{project['latest_release'] or '-'} | {project['license'] or '-'} | {flags} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="parse README only, no API calls")
    parser.add_argument("--limit", type=int, default=0, help="query at most N repos (testing)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    repos = parse_repos((root / "README.md").read_text(encoding="utf-8"))
    print(f"parsed {len(repos)} project repositories from README.md")

    if args.dry_run:
        return 0
    if not args.limit and len(repos) < MIN_REPOS:
        print(f"abort: fewer than {MIN_REPOS} repositories parsed", file=sys.stderr)
        return 1

    token = os.environ.get("GITHUB_TOKEN") or None
    now = datetime.now(timezone.utc)
    selected = repos[: args.limit] if args.limit else repos
    projects = [build_entry(owner, name, token, now) for owner, name in selected]
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
    data_path = root / "data" / "upstream-status.json"
    previous = json.loads(data_path.read_text(encoding="utf-8")) if data_path.exists() else {}
    if previous.get("projects") == projects:
        print("no changes")
        return 0

    data = {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": summary,
        "projects": projects,
    }
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    doc_path = root / "docs" / "upstream-status.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(render_markdown(data), encoding="utf-8")
    print(f"updated: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
