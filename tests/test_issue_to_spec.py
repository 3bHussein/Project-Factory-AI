import importlib.util
import pathlib
import unittest
spec = importlib.util.spec_from_file_location("intake", pathlib.Path(__file__).resolve().parents[1]/"scripts"/"issue_to_spec.py")
intake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(intake)
class IntakeTests(unittest.TestCase):
    def test_slug(self):
        self.assertEqual(intake.slugify("Task M!"),"task-m")
    def test_spec(self):
        value=intake.build_spec({"number":23,"title":"Task M","body":"Windows and Linux task manager","html_url":"https://github.com/example/repo/issues/23"})
        self.assertIn("Windows and Linux",value)
        self.assertIn("NOT generated application code",value)
    def test_empty_body(self):
        with self.assertRaises(ValueError):
            intake.build_spec({"number":2,"title":"Task","body":"","html_url":"https://example.com"})
if __name__=="__main__":
    unittest.main()
