#!/usr/bin/env python3
"""Read-only local listening-port inspector (Python standard library)."""
import argparse
import csv
import io
import json
import re
import shutil
import subprocess
import sys

def parse_ss(output):
    records = []
    for line in output.splitlines():
        parts = line.split(None, 6)
        if len(parts) < 5 or parts[0] not in ("tcp", "udp") or parts[1] != "LISTEN" and parts[0] == "tcp":
            continue
        address = parts[4]
        match = re.search(r":(\d+)$", address)
        if not match:
            continue
        records.append({"protocol": parts[0], "local_address": address, "port": int(match.group(1)), "pid": None})
    return records

def parse_netstat_windows(output):
    records = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) < 4 or parts[0].upper() not in ("TCP", "UDP"):
            continue
        protocol = parts[0].lower()
        if protocol == "tcp" and (len(parts) < 5 or parts[3].upper() != "LISTENING"):
            continue
        address = parts[1]
        match = re.search(r":(\d+)$", address)
        if not match:
            continue
        try:
            pid = int(parts[-1])
        except ValueError:
            pid = None
        records.append({"protocol": protocol, "local_address": address, "port": int(match.group(1)), "pid": pid})
    return records

def inspect(platform=None, runner=subprocess.run):
    platform = platform or sys.platform
    if platform.startswith("win"):
        command = ["netstat", "-ano", "-p", "tcp"]
        parser = parse_netstat_windows
    elif shutil.which("ss"):
        command = ["ss", "-lntu"]
        parser = parse_ss
    else:
        raise RuntimeError("No supported port inspection utility found (expected ss on Linux)")
    result = runner(command, capture_output=True, text=True, check=False, timeout=15, errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Inspection command failed")
    return sorted(parser(result.stdout), key=lambda r: (r["port"], r["protocol"], r["local_address"]))

def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only local listening-port inspector")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--port", type=int, help="Filter by local port")
    args = parser.parse_args(argv)
    if args.port is not None and not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")
    try:
        records = inspect()
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print("Inspection error: " + str(exc), file=sys.stderr)
        return 1
    if args.port is not None:
        records = [r for r in records if r["port"] == args.port]
    if args.json:
        print(json.dumps(records, indent=2))
    else:
        writer = csv.writer(sys.stdout)
        writer.writerow(["protocol", "local_address", "port", "pid"])
        for item in records:
            writer.writerow([item["protocol"], item["local_address"], item["port"], item["pid"] or ""])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
