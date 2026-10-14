"""Validate an external coding agent's output before allowing a review PR.

This module DOES NOT generate code or invoke an AI provider.
"""
import argparse
import pathlib
import subprocess
import sys

REQUIRED = ("README.md", "INSTALLATION.md", "USER-GUIDE.md",
            "ARCHITECTURE.md", "API-CLI.md", "SECURITY.md",
            "TEST-REPORT.md", "CHANGELOG.md", "DEVELOPMENT-LOG.md",
            "HANDOVER.md")

def validate_project(root, slug):
    if not slug or not all(c.isascii() and (c.islower() or c.isdigit() or c == "-") for c in slug) or slug.startswith("-") or slug.endswith("-"):
        raise ValueError("Invalid project slug")
    base = root.resolve()
    project = (base / "projects" / slug).resolve()
    if project.parent != (base / "projects").resolve() or not project.is_dir():
        raise ValueError("Project directory not found")
    missing = [name for name in REQUIRED if not (project / name).is_file()]
    if missing:
        raise ValueError("Missing required documentation: " + ", ".join(missing))
    if not any(p.is_file() for p in project.rglob("test_*.py")):
        raise ValueError("No automated Python test files found")
    return project

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    args = parser.parse_args(argv)
    project = validate_project(args.root, args.slug)
    print("Agent output structure validated:", project)
    return 0

if __name__ == "__main__":
    sys.exit(main())
