# CLI API

`python log_analyzer.py FILE [--html OUTPUT.html] [--json]`. JSON keys: total_lines, parsed_lines, invalid_lines, status_codes (object), top_error_paths (array of path/count). Exit 0 for success, 1 for file access/write failure. Python functions: `analyze(lines)` and `report_html(summary)`. No HTTP API.
