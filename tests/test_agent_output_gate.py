import importlib.util
import pathlib
import tempfile
import unittest

module_path = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "agent_output_gate.py"
spec = importlib.util.spec_from_file_location("agent_output_gate", module_path)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class AgentOutputGateTests(unittest.TestCase):
    def test_missing_project(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaisesRegex(ValueError, "not found"):
                gate.validate_project(pathlib.Path(root), "task-m")
    def test_reject_traversal(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaisesRegex(ValueError, "Invalid"):
                gate.validate_project(pathlib.Path(root), "../bad")
    def test_missing_docs(self):
        with tempfile.TemporaryDirectory() as root:
            project = pathlib.Path(root) / "projects" / "task-m"
            project.mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "documentation"):
                gate.validate_project(pathlib.Path(root), "task-m")
    def test_accept_complete_structure(self):
        with tempfile.TemporaryDirectory() as root:
            project = pathlib.Path(root) / "projects" / "task-m"
            project.mkdir(parents=True)
            for name in gate.REQUIRED:
                (project / name).write_text("placeholder")
            (project / "test_task_m.py").write_text("def test_basic(): assert True")
            self.assertEqual(gate.validate_project(pathlib.Path(root), "task-m"), project.resolve())
if __name__ == "__main__":
    unittest.main()
