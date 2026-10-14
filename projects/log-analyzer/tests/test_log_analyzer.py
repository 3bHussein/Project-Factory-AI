import importlib.util
import pathlib
import tempfile
import unittest
SPEC = importlib.util.spec_from_file_location("log_analyzer", pathlib.Path(__file__).resolve().parents[1] / "log_analyzer.py")
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)
LINE = '127.0.0.1 - - [14/Oct/2026:10:00:00 +0000] "GET /missing?secret=abc HTTP/1.1" 404 120'
class Tests(unittest.TestCase):
    def test_status_and_error_path(self):
        result = tool.analyze([LINE, LINE.replace("404", "200")])
        self.assertEqual(result["status_codes"], {"200":1, "404":1})
        self.assertEqual(result["top_error_paths"], [{"path":"/missing","count":1}])
    def test_invalid_line(self):
        self.assertEqual(tool.analyze(["bad line"])["invalid_lines"], 1)
    def test_html_escaping(self):
        report = tool.report_html({"total_lines":1,"parsed_lines":1,"invalid_lines":0,"status_codes":{"404":1},"top_error_paths":[{"path":"<script>alert(1)</script>","count":1}]})
        self.assertNotIn("<script>",report)
        self.assertIn("&lt;script&gt;",report)
    def test_cli_html_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = pathlib.Path(tmp)/"access.log"
            output = pathlib.Path(tmp)/"report.html"
            source.write_text(LINE+"\n",encoding="utf-8")
            self.assertEqual(tool.main([str(source),"--html",str(output)]),0)
            self.assertTrue(output.exists())
    def test_missing_file(self):
        self.assertEqual(tool.main(["does-not-exist-access-log.log"]),1)
if __name__=="__main__":
    unittest.main()
