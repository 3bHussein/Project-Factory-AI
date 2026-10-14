import datetime
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BacklogTests(unittest.TestCase):
    def test_unique_slugs(self):
        ideas = json.loads((ROOT / "ideas/backlog.json").read_text(encoding="utf-8"))
        self.assertGreater(len(ideas), 0)
        self.assertEqual(len(ideas), len({x["slug"] for x in ideas}))

    def test_required_fields(self):
        for idea in json.loads((ROOT / "ideas/backlog.json").read_text(encoding="utf-8")):
            for key in ("slug", "name", "problem", "platform", "language", "mvp"):
                self.assertTrue(idea.get(key), (idea, key))


if __name__ == "__main__":
    unittest.main()
