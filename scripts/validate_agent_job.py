"""Validate coding job manifests before handing them to an approved worker.

Validation does not execute untrusted content or start any AI service.
"""
import argparse
import json
import pathlib
import re

def validate_job(job, root):
    if not isinstance(job, dict) or job.get("schema_version") != 1:
        raise ValueError("Unsupported job manifest schema")
    number = job.get("issue_number")
    slug = job.get("project_slug")
    if type(number) is not int or number < 1:
        raise ValueError("Invalid issue number")
    if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Invalid slug")
    if job.get("state") != "awaiting_agent" or job.get("provider") is not None:
        raise ValueError("Job is not awaiting an approved provider")
    if job.get("paid_api_enabled") is not False or job.get("auto_merge") is not False:
        raise ValueError("Unsafe job permissions")
    expected = f"projects/{slug}"
    if job.get("output_directory") != expected:
        raise ValueError("Unexpected output directory")
    spec = job.get("specification_path")
    if not isinstance(spec, str) or not (spec.startswith(f"requests/issue-{number}-") and spec.endswith(".md") and re.fullmatch(r"[a-z0-9-]+", spec[len(f"requests/issue-{number}-"):-3])):
        raise ValueError("Invalid specification path")
    if int(spec.split("/issue-", 1)[1].split("-", 1)[0]) != number:
        raise ValueError("Issue number mismatch")
    root = pathlib.Path(root).resolve()
    spec_file = (root / spec).resolve()
    if not spec_file.is_relative_to(root / "requests") or not spec_file.is_file():
        raise ValueError("Specification not found")
    if not spec_file.read_text(encoding="utf-8").strip():
        raise ValueError("Specification is empty")
    return spec_file

def main():
    p = argparse.ArgumentParser()
    p.add_argument("job", type=pathlib.Path)
    p.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    args = p.parse_args()
    job = json.loads(args.job.read_text(encoding="utf-8"))
    print("Validated queued job:", validate_job(job, args.root))
if __name__ == "__main__":
    main()
