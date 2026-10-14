#!/usr/bin/env python3
"""Offline deterministic project generator; no AI API or paid services."""
import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ("README.md", "ARCHITECTURE.md", "INSTALLATION.md", "USER-GUIDE.md", "API.md", "SECURITY.md", "TEST-REPORT.md", "CHANGELOG.md", "DEVELOPMENT-LOG.md", "HANDOVER.md")
VALID = re.compile(r"^[a-z][a-z0-9-]{2,49}$")

def generate(slug, name, output_root, overwrite=False):
    if not VALID.fullmatch(slug):
        raise ValueError("Slug must be 3-50 lowercase letters, digits or hyphens, starting with a letter")
    dest = pathlib.Path(output_root) / slug
    if dest.exists() and any(dest.iterdir()) and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing project: {dest}")
    dest.mkdir(parents=True, exist_ok=True)
    module = slug.replace("-", "_")
    date = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    code = '''#!/usr/bin/env python3
"""Simple offline text statistics tool."""
import argparse
import json
import pathlib

def analyze(text):
    return {"characters": len(text), "words": len(text.split()), "lines": len(text.splitlines())}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline text statistics")
    parser.add_argument("file", type=pathlib.Path, help="UTF-8 text file to inspect")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        data = analyze(args.file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.exit(1, f"Cannot read input: {exc}\\n")
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        for key, value in data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
'''
    tests = f'''import importlib.util
import pathlib
import unittest

path = pathlib.Path(__file__).resolve().parents[1] / "{module}.py"
spec = importlib.util.spec_from_file_location("generated_tool", path)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)

class ToolTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(tool.analyze(""), {{"characters": 0, "words": 0, "lines": 0}})

    def test_words(self):
        self.assertEqual(tool.analyze("hello world\\n")["words"], 2)

if __name__ == "__main__":
    unittest.main()
'''
    docs = {
        "README.md": f"# {name}\\n\\nOffline text statistics CLI built from a reviewed Python template. Counts characters, words and lines from UTF-8 files. No internet connection, API keys or paid services required.\\n\\nUsage: `python {module}.py example.txt --json`.\\n",
        "ARCHITECTURE.md": f"# Architecture\\n\\nThe `{module}.py` command parses CLI arguments, reads one local UTF-8 file and calls a pure `analyze(text)` function. It prints results to the terminal. No databases, network services, plugins or background processes are involved.\\n",
        "INSTALLATION.md": f"# Installation\\n\\nRequires Python 3.10 or newer on Windows or Linux. No pip packages are needed. Download the project folder, open a terminal in it and run `python {module}.py --help`. On Linux, use `python3` if needed.\\n",
        "USER-GUIDE.md": f"# User Guide\\n\\nCreate a UTF-8 text file named `example.txt`. Run `python {module}.py example.txt` for readable counts, or add `--json` for machine-readable output. An unreadable or invalid file exits with an error.\\n",
        "API.md": f"# CLI API\\n\\nThere is no HTTP API. `python {module}.py FILE [--json]` accepts a local UTF-8 file. Output fields are `characters`, `words` and `lines`, all integers. The pure Python function `analyze(text: str)` returns a dictionary with the same keys.\\n",
        "SECURITY.md": "# Security\\n\\nReads only a user-specified local text file. No remote requests, shell commands, privilege escalation, file modifications or secrets are required. Avoid supplying sensitive files if terminal output or logs may be shared.\\n",
        "TEST-REPORT.md": f"# Test Report\\n\\nRun `python -m unittest discover -s tests -v`. Tests cover empty and two-word input. CI execution for this generated project has not yet been verified. Record actual Windows/Linux results here after testing; do not claim unverified results.\\n",
        "CHANGELOG.md": f"# Changelog\\n\\n## 0.1.0 — {date}\\n\\nInitial offline text statistics CLI generated from the standard-library template. This is a starter implementation, not an AI-created arbitrary project.\\n",
        "DEVELOPMENT-LOG.md": f"# Development Log\\n\\n## {date}\\n\\nGenerated from the reviewed offline Python CLI template by `scripts/generate_project.py`. No AI API used and no existing project overwritten. Follow-up: run tests on supported platforms, review behavior and record outcomes.\\n",
        "HANDOVER.md": f"# Handover\\n\\nStart with README.md and ARCHITECTURE.md. Run `python -m unittest discover -s tests -v`, then inspect `{module}.py` and its CLI help. Keep functionality offline and read-only unless explicitly approved. Update CHANGELOG.md and DEVELOPMENT-LOG.md with future changes.\\n"
    }
    # Normalize escaped newlines in generated Markdown strings.
    for filename, value in docs.items():
        (dest / filename).write_text(value.replace("\\n", "\n"), encoding="utf-8")
    (dest / f"{module}.py").write_text(code, encoding="utf-8")
    (dest / "tests").mkdir(exist_ok=True)
    (dest / "tests" / "test_tool.py").write_text(tests, encoding="utf-8")
    return dest

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--output", type=pathlib.Path, default=ROOT / "projects")
    args = parser.parse_args(argv)
    try:
        dest = generate(args.slug, args.name, args.output)
    except (ValueError, FileExistsError) as exc:
        parser.error(str(exc))
    print(json.dumps({"project": str(dest), "generated": True, "type": "reviewed-template", "ai": False}))

if __name__ == "__main__":
    main()
