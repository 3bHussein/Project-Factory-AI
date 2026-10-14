import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate_projects.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class ValidationTests(unittest.TestCase):
    def test_rejects_missing_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = pathlib.Path(tmp) / "sample"
            p.mkdir()
            self.assertTrue(any("README.md" in x for x in validator.validate(pathlib.Path(tmp))))

    def test_accepts_complete_structure(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = pathlib.Path(tmp) / "sample"
            p.mkdir()
            for name in validator.REQUIRED:
                (p / name).write_text("Complete documentation section with enough useful detail.\n", encoding="utf-8")
            (p / "tests").mkdir()
            (p / "tests/test_sample.py").write_text("def test_example(): pass\n")
            self.assertEqual(validator.validate(pathlib.Path(tmp)), [])

if __name__ == "__main__":
    unittest.main()
