#!/usr/bin/env python3
"""Check that every delivered project contains complete documentation and tests."""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = ("README.md", "ARCHITECTURE.md", "INSTALLATION.md", "USER-GUIDE.md", "API.md", "SECURITY.md", "TEST-REPORT.md", "CHANGELOG.md", "DEVELOPMENT-LOG.md", "HANDOVER.md")

def validate(base):
    failures = []
    if not base.is_dir():
        return [f"Missing projects directory: {base}"]
    for project in sorted(x for x in base.iterdir() if x.is_dir()):
        for name in REQUIRED:
            path = project / name
            if not path.is_file() or len(path.read_text(encoding="utf-8").strip()) < 40:
                failures.append(f"{project.name}: missing or incomplete {name}")
        if not (project / "tests").is_dir() or not list((project / "tests").glob("test_*.py")):
            failures.append(f"{project.name}: missing Python unit tests")
    return failures

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--projects-dir", type=pathlib.Path, default=ROOT / "projects")
    args = parser.parse_args(argv)
    problems = validate(args.projects_dir)
    for problem in problems:
        print("FAIL:", problem)
    if problems:
        return 1
    print("Project documentation and test structure validated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
