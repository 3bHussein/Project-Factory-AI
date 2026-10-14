# Port Inspector V1

Read-only command-line utility to list local listening TCP/UDP ports. Uses the Python standard library, `ss` on Linux, and `netstat` on Windows. Does **not** scan remote machines or change firewall settings.

## Usage

```bash
python port_inspector.py
python port_inspector.py --json
python port_inspector.py --port 8080
python -m unittest discover -s tests -v
```

Output defaults to CSV, useful for scripts. Linux `ss` version currently does not return PIDs. Windows currently queries listening TCP only (UDP planned). Supported: Windows and Linux with `ss`; macOS not supported yet. Treat output as sensitive when sharing it because it reveals local services.
