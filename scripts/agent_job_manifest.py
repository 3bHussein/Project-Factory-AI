"""Create a safe, provider-neutral coding job manifest from an approved request.

This does not invoke a coding model or run untrusted issue content.
"""
import argparse
import json
import pathlib
import re

def make_manifest(issue_number, slug, spec_path):
    if not isinstance(issue_number, int) or issue_number < 1:
        raise ValueError("Invalid issue number")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Invalid project slug")
    path = pathlib.PurePosixPath(spec_path)
    if (path.is_absolute() or ".." in path.parts or
            not str(path).startswith("requests/") or path.suffix != ".md"):
        raise ValueError("Specification must be a markdown file in requests/")
    return {
        "schema_version": 1,
        "issue_number": issue_number,
        "project_slug": slug,
        "specification_path": str(path),
        "state": "awaiting_agent",
        "provider": None,
        "paid_api_enabled": False,
        "auto_merge": False,
        "output_directory": f"projects/{slug}",
        "required_checks": ["agent-output", "quality-windows", "quality-linux", "human-review"]
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--issue-number", required=True, type=int)
    p.add_argument("--slug", required=True)
    p.add_argument("--spec", required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    args = p.parse_args()
    manifest = make_manifest(args.issue_number, args.slug, args.spec)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(args.out)
if __name__ == "__main__":
    main()
