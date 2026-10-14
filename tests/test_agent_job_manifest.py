import importlib.util
import pathlib
import unittest
spec = importlib.util.spec_from_file_location("manifest", pathlib.Path(__file__).resolve().parents[1]/"scripts"/"agent_job_manifest.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
class ManifestTests(unittest.TestCase):
    def test_valid(self):
        x=mod.make_manifest(42,"task-m","requests/issue-42-task-m.md")
        self.assertEqual(x["state"],"awaiting_agent")
        self.assertIsNone(x["provider"])
        self.assertFalse(x["paid_api_enabled"])
        self.assertFalse(x["auto_merge"])
    def test_bad_slug(self):
        with self.assertRaises(ValueError): mod.make_manifest(42,"../other","requests/x.md")
    def test_bad_spec(self):
        with self.assertRaises(ValueError): mod.make_manifest(42,"task-m","../secret.md")
    def test_bad_issue(self):
        with self.assertRaises(ValueError): mod.make_manifest(0,"task-m","requests/x.md")
if __name__=="__main__": unittest.main()
