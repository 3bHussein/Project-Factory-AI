# Log Analyzer V1

Offline, read-only Apache/Nginx access-log analyzer for Windows and Linux. Summarizes HTTP status codes, counts invalid lines, finds the top 20 error URL paths and exports an HTML report. No logs are uploaded or transmitted. Requires Python 3.10+ only.

Run `python log_analyzer.py access.log --html report.html` or `python log_analyzer.py access.log --json`.
