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


class FormatStarsTests(unittest.TestCase):
    def test_thousands_with_one_decimal(self):
        self.assertEqual(tu.format_stars(1200), "1.2k")
        self.assertEqual(tu.format_stars(49778), "49.8k")
        self.assertEqual(tu.format_stars(1000), "1.0k")

    def test_small_counts_show_as_under_one_k(self):
        self.assertEqual(tu.format_stars(999), "<1k")
        self.assertEqual(tu.format_stars(0), "<1k")

    def test_growth_is_signed_and_abbreviated(self):
        self.assertEqual(tu.format_growth(7463), "+7.5k")
        self.assertEqual(tu.format_growth(600), "+0.6k")
        self.assertEqual(tu.format_growth(1835), "+1.8k")
        self.assertEqual(tu.format_growth(3), "+0.1k")


class DecorateLineTests(unittest.TestCase):
    def test_adds_badges_and_replaces_previous_suffix(self):
        line = "- [name](https://github.com/owner/name) - desc <sub>old</sub>"
        index = {"owner/name": project()}
        self.assertEqual(
            tu.decorate_line(line, index),
            "- [name](https://github.com/owner/name) - desc <sub>更新 2026-10-19 · ★ 1.2k · MIT</sub>",
        )

    def test_unknown_status_keeps_line(self):
        line = "- [name](https://github.com/owner/name) - desc"
        self.assertEqual(tu.decorate_line(line, {"owner/name": project(status="unknown")}), line)

    def test_non_project_line_is_untouched(self):
        line = "## Heading"
        self.assertEqual(tu.decorate_line(line, {}), line)


class GrowthBoardTests(unittest.TestCase):
    def test_collecting_message_without_a_baseline_snapshot(self):
        history = {"2026-10-20": {"owner/name": 100}}
        self.assertIn("数据积累中", tu.render_growth_board([project()], history, NOW))

    def test_english_labels_for_messages(self):
        history = {"2026-10-20": {"owner/name": 100}}
        self.assertIn("Collecting data", tu.render_growth_board([project()], history, NOW, tu.LABELS["en"]))

    def test_ranks_by_gain_and_skips_non_growth_and_unbaselined(self):
        history = {
            "2026-10-13": {"a/a": 1000, "b/b": 500, "c/c": 900, "d/d": 100},
            "2026-10-19": {"a/a": 1100},
        }
        projects = [
            project(repo="a/a", url="https://github.com/a/a", stars=1500),
            project(repo="b/b", url="https://github.com/b/b", stars=1000),
            project(repo="c/c", url="https://github.com/c/c", stars=900),
            project(repo="d/d", url="https://github.com/d/d", stars=50),
            project(repo="e/e", url="https://github.com/e/e", stars=10),
        ]
        board = tu.render_growth_board(projects, history, NOW)
        self.assertIn("2026-10-13 → 2026-10-20", board)
        self.assertLess(board.index("a/a"), board.index("b/b"))  # tie on +500: more stars first
        self.assertIn("+0.5k ★", board)
        for absent in ("c/c", "d/d", "e/e"):
            self.assertNotIn(absent, board)

    def test_board_is_capped_at_board_size(self):
        history = {"2026-10-13": {f"o/r{i}": 0 for i in range(tu.BOARD_SIZE + 5)}}
        projects = [project(repo=f"o/r{i}", url=f"https://github.com/o/r{i}", stars=i + 1) for i in range(tu.BOARD_SIZE + 5)]
        board = tu.render_growth_board(projects, history, NOW)
        self.assertEqual(sum(1 for line in board.split("\n") if line[:1].isdigit()), tu.BOARD_SIZE)


class HistoryTests(unittest.TestCase):
    def test_adds_today_and_keeps_last_history_days(self):
        history = {f"2026-10-{d:02d}": {} for d in range(1, 20)}
        result = tu.update_history(history, [project(stars=5)], NOW)
        self.assertEqual(len(result), tu.HISTORY_DAYS)
        self.assertEqual(result["2026-10-20"], {"owner/name": 5})
        self.assertNotIn("2026-10-01", result)


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
