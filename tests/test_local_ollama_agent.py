import importlib.util
import pathlib
import sys
import unittest
root = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "scripts"))
spec = importlib.util.spec_from_file_location("local_agent", root / "scripts" / "local_ollama_agent.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class LocalAgentTests(unittest.TestCase):
    def test_accept(self):
        x=mod.safe_files({"files":[{"path":"projects/task-m/main.py","content":"print(1)"}]},"task-m")
        self.assertIn("projects/task-m/main.py",x)
    def test_reject_other_project(self):
        with self.assertRaises(ValueError):
            mod.safe_files({"files":[{"path":"projects/other/main.py","content":"x"}]},"task-m")
    def test_reject_traversal(self):
        with self.assertRaises(ValueError):
            mod.safe_files({"files":[{"path":"projects/task-m/../../bad.py","content":"x"}]},"task-m")
    def test_reject_hidden(self):
        with self.assertRaises(ValueError):
            mod.safe_files({"files":[{"path":"projects/task-m/.github/workflows/x.yml","content":"x"}]},"task-m")
    def test_reject_duplicate(self):
        with self.assertRaises(ValueError):
            mod.safe_files({"files":[{"path":"projects/task-m/a.py","content":"a"},{"path":"projects/task-m/a.py","content":"b"}]},"task-m")
if __name__ == "__main__":
    unittest.main()
