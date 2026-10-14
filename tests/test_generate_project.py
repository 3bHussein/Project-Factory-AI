import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generator", ROOT / "scripts/generate_project.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)

class GeneratorTests(unittest.TestCase):
    def test_generates_code_docs_tests(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = generator.generate("text-statistics", "Text Statistics", tmp)
            self.assertTrue((dest / "text_statistics.py").exists())
            self.assertTrue((dest / "tests/test_tool.py").exists())
            for doc in generator.DOCS:
                self.assertTrue((dest / doc).exists(), doc)

    def test_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            generator.generate("text-statistics", "Text Statistics", tmp)
            with self.assertRaises(FileExistsError):
                generator.generate("text-statistics", "Text Statistics", tmp)

    def test_rejects_invalid_slug(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                generator.generate("../unsafe", "Unsafe", tmp)

if __name__ == "__main__":
    unittest.main()
