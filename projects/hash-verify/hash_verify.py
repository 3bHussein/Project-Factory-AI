#!/usr/bin/env python3
"""Read-only streaming file hash calculator and verifier."""
import argparse
import hashlib
import json
import pathlib
import re
import sys

ALGORITHMS = ("sha256", "sha512")
CHUNK_SIZE = 1024 * 1024

def hash_file(path, algorithm="sha256"):
    if algorithm not in ALGORITHMS:
        raise ValueError("Unsupported hash algorithm")
    digest = hashlib.new(algorithm)
    with open(path, "rb") as source:
        for chunk in iter(lambda: source.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()

def verify_file(path, expected, algorithm="sha256"):
    length = hashlib.new(algorithm).digest_size * 2
    if len(expected) != length or not re.fullmatch(r"[0-9a-fA-F]+", expected):
        raise ValueError(f"Expected {length} hexadecimal characters for {algorithm}")
    actual = hash_file(path, algorithm)
    return actual.lower() == expected.lower(), actual

def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculate or verify a local file hash")
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("--algorithm", choices=ALGORITHMS, default="sha256")
    parser.add_argument("--expected", help="Expected hexadecimal digest to verify")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.expected is None:
            actual = hash_file(args.file, args.algorithm)
            output = {"file": str(args.file), "algorithm": args.algorithm, "hash": actual}
            code = 0
        else:
            matched, actual = verify_file(args.file, args.expected, args.algorithm)
            output = {"file": str(args.file), "algorithm": args.algorithm, "hash": actual, "matched": matched}
            code = 0 if matched else 2
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print(f"{args.algorithm.upper()}: {actual}")
        if args.expected is not None:
            print("MATCH" if output["matched"] else "MISMATCH")
    return code

if __name__ == "__main__":
    raise SystemExit(main())
