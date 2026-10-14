#!/usr/bin/env python3
"""Offline, read-only access-log analyzer (Apache/Nginx combined/common format)."""
import argparse
import collections
import html
import json
import pathlib
import re
import sys

ACCESS = re.compile(r'^\S+ \S+ \S+ \[[^]]+\] "(?P<request>[^"]*)" (?P<status>\d{3}) (?:\d+|-)')
def analyze(lines):
    statuses = collections.Counter()
    paths = collections.Counter()
    total = invalid = 0
    for line in lines:
        total += 1
        match = ACCESS.match(line.strip())
        if not match:
            invalid += 1
            continue
        status = int(match.group("status"))
        statuses[str(status)] += 1
        if status >= 400:
            parts = match.group("request").split()
            path = parts[1] if len(parts) >= 2 else "(unknown)"
            paths[path.split("?")[0]] += 1
    return {"total_lines": total, "parsed_lines": total-invalid, "invalid_lines": invalid,
            "status_codes": dict(sorted(statuses.items())),
            "top_error_paths": [{"path": path, "count": count} for path, count in paths.most_common(20)]}
def report_html(summary):
    rows = "".join("<tr><td>"+html.escape(k)+"</td><td>"+str(v)+"</td></tr>" for k,v in summary["status_codes"].items())
    paths = "".join("<tr><td>"+html.escape(x["path"])+"</td><td>"+str(x["count"])+"</td></tr>" for x in summary["top_error_paths"])
    return ('<!doctype html><html lang="en"><meta charset="utf-8"><title>Local Log Report</title>'
            '<style>body{font:16px system-ui;max-width:850px;margin:3rem auto;padding:1rem}table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:.5rem;text-align:left}</style>'
            '<h1>Local Log Report</h1><p>Lines: '+str(summary["total_lines"])+
            ' | Parsed: '+str(summary["parsed_lines"])+
            ' | Invalid: '+str(summary["invalid_lines"])+
            '</p><h2>HTTP status codes</h2><table><tr><th>Status</th><th>Count</th></tr>'+rows+
            '</table><h2>Most common error paths</h2><table><tr><th>Path</th><th>Count</th></tr>'+paths+'</table></html>')
def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline Apache/Nginx access-log report")
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("--html", type=pathlib.Path, help="Save HTML report locally")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        with args.file.open(encoding="utf-8", errors="replace") as source:
            summary = analyze(source)
        if args.html:
            args.html.write_text(report_html(summary), encoding="utf-8")
    except OSError as exc:
        print("Error: "+str(exc), file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print("Lines:", summary["total_lines"], "| Parsed:", summary["parsed_lines"], "| Invalid:", summary["invalid_lines"])
        for status,count in summary["status_codes"].items():
            print(status, count)
        if args.html:
            print("HTML report:", args.html)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
