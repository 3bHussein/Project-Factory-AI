# User Guide

Run `python log_analyzer.py access.log --html report.html` to produce an offline HTML report. Open the saved HTML file in any browser. Run with `--json` for a machine-readable summary. The input must be Apache/Nginx common or combined access-log format; unrelated formats are counted as invalid lines. Output includes HTTP status counts and top error URL paths, with query strings omitted.
