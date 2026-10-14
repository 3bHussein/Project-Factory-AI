# CLI API

Command: `python hash_verify.py FILE [--algorithm sha256|sha512] [--expected HEXDIGEST] [--json]`. JSON fields: `file`, `algorithm`, `hash`, and optionally `matched` (boolean). Exit codes: 0 for calculation success or verification match, 2 for digest mismatch, 1 for file access or input validation error. `hash_file(path, algorithm)` and `verify_file(path, expected, algorithm)` are importable Python functions.
