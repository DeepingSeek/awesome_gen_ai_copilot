import unittest
from datetime import datetime, timezone

import track_upstream as tu

NOW = datetime(2026, 10, 20, tzinfo=timezone.utc)


def project(**overrides):
    base = {
        "repo": "owner/name",
        "url": "https://github.com/owner/name",
        "status": "ok",
        "stars": 1200,
        "pushed_at": "2026-10-19T08:00:00Z",
        "archived": False,
        "license": "MIT",
        "tracked_update": None,
        "update_type": None,
        "update_summary": "",
    }
    base.update(overrides)
    return base


class DecorateLineTests(unittest.TestCase):
    def test_adds_badges_and_replaces_previous_suffix(self):
        line = "- [name](https://github.com/owner/name) - desc <sub>old</sub>"
        index = {"owner/name": project()}
        self.assertEqual(
            tu.decorate_line(line, index),
            "- [name](https://github.com/owner/name) - desc <sub>更新 2026-10-19 · ★ 1200 · MIT</sub>",
        )

    def test_unknown_status_keeps_line(self):
        line = "- [name](https://github.com/owner/name) - desc"
        self.assertEqual(tu.decorate_line(line, {"owner/name": project(status="unknown")}), line)

    def test_non_project_line_is_untouched(self):
        line = "## Heading"
        self.assertEqual(tu.decorate_line(line, {}), line)


class BoardTests(unittest.TestCase):
    def test_empty_board_message(self):
        self.assertIn("暂无更新", tu.render_board([project()], NOW))

    def test_only_recent_entries_sorted_newest_first(self):
        recent = project(repo="a/a", url="https://github.com/a/a",
                         tracked_update="2026-10-18T10:00:00Z", update_type="commit", update_summary="fix")
        newer = project(repo="b/b", url="https://github.com/b/b",
                        tracked_update="2026-10-19T10:00:00Z", update_type="release", update_summary="v2")
        old = project(repo="c/c", url="https://github.com/c/c",
                      tracked_update="2026-10-01T10:00:00Z", update_type="commit", update_summary="old")
        board = tu.render_board([recent, newer, old], NOW)
        self.assertLess(board.index("b/b"), board.index("a/a"))
        self.assertNotIn("c/c", board)
        self.assertIn("Release", board)


class ApplyReadmeTests(unittest.TestCase):
    def test_requires_markers(self):
        self.assertIsNone(tu.apply_readme("no markers", [], "x"))

    def test_replaces_board_and_is_idempotent(self):
        text = (
            f"{tu.BOARD_BEGIN}\nold\n{tu.BOARD_END}\n"
            "- [name](https://github.com/owner/name) - desc\n"
        )
        first = tu.apply_readme(text, [project()], "NEW")
        self.assertIn(f"{tu.BOARD_BEGIN}\nNEW\n{tu.BOARD_END}", first)
        self.assertEqual(tu.apply_readme(first, [project()], "NEW"), first)


class SummaryTests(unittest.TestCase):
    def test_release_summary_skips_headings(self):
        body = "## Changes\n\nAdd **streaming** support with [docs](https://x.y)\n\nmore"
        self.assertEqual(tu.release_summary(body), "Add streaming support with docs")

    def test_commit_summary_joins_first_lines(self):
        self.assertEqual(tu.commit_summary(["fix a\n\nbody", "add b"]), "fix a；add b")

    def test_commit_summary_fallback(self):
        self.assertEqual(tu.commit_summary([]), "仓库有新推送")


if __name__ == "__main__":
    unittest.main()
