import importlib.util
import pathlib
import unittest

MODULE = pathlib.Path(__file__).resolve().parents[1] / "port_inspector.py"
spec = importlib.util.spec_from_file_location("port_inspector", MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ParserTests(unittest.TestCase):
    def test_linux_ss_tcp_and_udp(self):
        sample = ("Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process\n"
                  "tcp LISTEN 0 128 127.0.0.1:8080 0.0.0.0:*\n"
                  "udp UNCONN 0 0 0.0.0.0:5353 0.0.0.0:*\n")
        rows = mod.parse_ss(sample)
        self.assertEqual([(r["protocol"], r["port"]) for r in rows], [("tcp", 8080), ("udp", 5353)])

    def test_windows_netstat(self):
        sample = "  TCP    0.0.0.0:135    0.0.0.0:0    LISTENING    1234\n  TCP    127.0.0.1:444    1.2.3.4:555    ESTABLISHED    22\n"
        rows = mod.parse_netstat_windows(sample)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["pid"], 1234)
        self.assertEqual(rows[0]["port"], 135)

    def test_empty(self):
        self.assertEqual(mod.parse_ss(""), [])
        self.assertEqual(mod.parse_netstat_windows(""), [])

if __name__ == "__main__":
    unittest.main()
