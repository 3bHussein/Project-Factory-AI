# User Guide

Calculate a SHA-256 digest: `python hash_verify.py archive.zip`. For SHA-512: `python hash_verify.py archive.zip --algorithm sha512`. To check an expected digest obtained from a trusted source, add `--expected HEXDIGEST`. Add `--json` to print structured results. MATCH means the computed digest equals the expected digest; MISMATCH means it does not. Always obtain the expected digest through a trustworthy channel.
