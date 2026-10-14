import importlib.util
import pathlib
import tempfile
import unittest

rootpath = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("job_validation", rootpath / "scripts" / "validate_agent_job.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class JobValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "requests").mkdir()
        self.path = self.root / "requests" / "issue-9-task-m.md"
        self.path.write_text("# Task M")
        self.job = {"schema_version":1,"issue_number":9,"project_slug":"task-m",
                    "specification_path":"requests/issue-9-task-m.md",
                    "state":"awaiting_agent","provider":None,"paid_api_enabled":False,
                    "auto_merge":False,"output_directory":"projects/task-m"}
    def test_valid(self):
        self.assertEqual(module.validate_job(self.job,self.root),self.path.resolve())
    def test_missing_spec(self):
        self.path.unlink()
        with self.assertRaises(ValueError): module.validate_job(self.job,self.root)
    def test_wrong_issue(self):
        self.job["issue_number"]=8
        with self.assertRaises(ValueError): module.validate_job(self.job,self.root)
    def test_paid_api_rejected(self):
        self.job["paid_api_enabled"]=True
        with self.assertRaises(ValueError): module.validate_job(self.job,self.root)
    def test_path_traversal(self):
        self.job["specification_path"]="../secrets.md"
        with self.assertRaises(ValueError): module.validate_job(self.job,self.root)
if __name__=="__main__": unittest.main()
