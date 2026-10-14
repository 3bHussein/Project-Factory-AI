import importlib.util
import hashlib
import pathlib
import tempfile
import unittest

PATH = pathlib.Path(__file__).resolve().parents[1] / "hash_verify.py"
spec = importlib.util.spec_from_file_location("hash_verify", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class HashVerifyTests(unittest.TestCase):
    def test_sha256(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = pathlib.Path(tmp) / "test.bin"
            file.write_bytes(b"abc")
            self.assertEqual(mod.hash_file(file), hashlib.sha256(b"abc").hexdigest())

    def test_sha512(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = pathlib.Path(tmp) / "test.bin"
            file.write_bytes(b"abc")
            self.assertEqual(mod.hash_file(file, "sha512"), hashlib.sha512(b"abc").hexdigest())

    def test_verify_match_and_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = pathlib.Path(tmp) / "test.bin"
            file.write_bytes(b"abc")
            good = hashlib.sha256(b"abc").hexdigest()
            self.assertTrue(mod.verify_file(file, good)[0])
            self.assertFalse(mod.verify_file(file, "0" * 64)[0])

    def test_rejects_bad_expected_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = pathlib.Path(tmp) / "test.bin"
            file.write_bytes(b"abc")
            with self.assertRaises(ValueError):
                mod.verify_file(file, "not-a-hash")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            mod.hash_file("missing-file-not-created-here.txt")

if __name__ == "__main__":
    unittest.main()
