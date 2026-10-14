# Hash Verify V1

A free, offline, read-only CLI for calculating SHA-256/SHA-512 file digests and checking downloads against a trusted published digest. Uses Python standard library and streams large files without loading the entire file into memory.

Examples: `python hash_verify.py download.zip` or `python hash_verify.py download.zip --expected <64-character-SHA256>`. JSON output is available with `--json`. A matching hash checks integrity relative to the expected digest, not the trustworthiness of its source.
