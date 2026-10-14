# Architecture

The CLI uses argparse for options, pathlib for paths and hashlib for SHA-256/SHA-512. It streams file bytes in 1 MiB blocks and computes a hexadecimal digest. Verification validates expected digest syntax and compares the computed digest. No network access, databases, or external dependencies. Exit codes distinguish match, mismatch and errors.
