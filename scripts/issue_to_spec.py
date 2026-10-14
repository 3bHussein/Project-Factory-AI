"""Convert a GitHub project-request issue into a reviewed specification file."""
import argparse
import json
import pathlib
import re
from agent_job_manifest import make_manifest

def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:60] or "project-request"

def build_spec(issue):
    title = issue.get("title", "").strip()
    body = issue.get("body") or ""
    number = int(issue["number"])
    if not title or not body.strip():
        raise ValueError("Issue title and body are required")
    # Keep untrusted issue content as plain text, never execute it.
    return ("# Project Request Specification\n\n"
            f"Source: {issue['html_url']}\n\n"
            f"Issue: #{number}\n\n"
            f"Title: {title}\n\n"
            "## User requirements (unreviewed)\n\n"
            + body + "\n\n"
            "## Implementation gate\n\n"
            "- [ ] Human review of scope, dependencies and risks\n"
            "- [ ] Distinct runnable project, not a renamed template\n"
            "- [ ] Automated tests on supported platforms\n"
            "- [ ] Ten required documentation files\n"
            "- [ ] Human review before merge\n\n"
            "This specification is NOT generated application code.\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--event", type=pathlib.Path, required=True)
    p.add_argument("--output-dir", type=pathlib.Path, default=pathlib.Path("requests"))
    args = p.parse_args()
    issue = json.loads(args.event.read_text(encoding="utf-8"))["issue"]
    number = int(issue["number"])
    if number < 1:
        raise ValueError("Invalid issue number")
    target = args.output_dir / f"issue-{number}-{slugify(issue['title'])}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build_spec(issue), encoding="utf-8")
    slug = slugify(issue["title"].removeprefix("[Project Request]").strip())
    job = make_manifest(number, slug, target.as_posix())
    job_target = target.with_suffix(".job.json")
    job_target.write_text(json.dumps(job, indent=2), encoding="utf-8")
    print(target)
    print(job_target)
if __name__ == "__main__":
    main()
