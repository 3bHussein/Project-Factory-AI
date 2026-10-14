# 🏭 Project Factory AI

**Project Factory AI is a free-first open-source factory for useful software tools.** It is not one desktop application. The repository contains the factory scripts, daily project ideas, real tools under `projects/`, automated tests, and documentation.

## How it works (simple explanation)

1. The daily GitHub Actions workflow chooses an idea and opens a **proposal** pull request for human review.
2. The separate starter generator creates a **real runnable Python text-statistics tool** with tests and 10 documentation files. It is currently a fixed template, not a general AI coder.
3. Quality gates run tests and check required documentation; changes are reviewed before merging into `main`.
4. Each tool has its own folder and user instructions. **No paid AI API, auto-merge, or automatic deployment is configured.**

> **Current limitation:** Daily automation generates **ideas/specifications**, not different finished programs every day. A general AI development agent has not been implemented.

## 🤖 No-code Project Builder\n\nOpen [AI Project Builder](dashboard/builder.html) (or use the Dashboard link), describe your idea in Arabic or English, review the structured specification and open a prefilled GitHub Issue. This is a **local browser-based specification helper**, not an AI coding agent; it does not upload the description to any external AI service or automatically write application code. GitHub receives the issue only after you choose to submit it.\n\n## 💡 Request a custom project\n\nUse the [custom project request form](https://github.com/3bHussein/Project-Factory-AI/issues/new/choose) to describe the problem, platform, features, example inputs/outputs and acceptance tests. Read the [request guide](docs/REQUEST-A-PROJECT.md). **Opening an issue does not yet automatically generate custom application code.** A developer or explicitly assigned coding agent must implement it and pass review.\n\n## 👀 Dashboard

Once GitHub Pages is enabled, visit **https://3bhussein.github.io/Project-Factory-AI/**. Until then, open [dashboard/index.html](dashboard/index.html) after downloading the repository. It is a responsive static project catalog and guide. It cannot execute local Python programs directly from the browser.

## Available projects

| Project | Purpose | Run |
| --- | --- | --- |
| [Port Inspector](projects/port-inspector/) | Read-only listing of local listening ports on Windows/Linux | `python projects/port-inspector/port_inspector.py --json` |
| [Log Analyzer](projects/log-analyzer/) | Offline access-log analysis and HTML reports | `python projects/log-analyzer/log_analyzer.py access.log --html report.html` |\n| [Hash Verify](projects/hash-verify/) | Offline SHA-256/SHA-512 checksums | `python projects/hash-verify/hash_verify.py myfile.zip --json` |\n| Text Statistics starter | Counts words, characters, and lines in a UTF-8 file | Generate it using the command below |

Tools in open pull requests are not part of `main` until merged.

## 🚀 Download and run (Windows / Linux)

Install Python 3.10+ and Git:

```bash
git clone https://github.com/3bHussein/Project-Factory-AI.git
cd Project-Factory-AI
python -m unittest discover -s tests -v
python scripts/validate_projects.py
```

On Linux, replace `python` with `python3` if needed. Port Inspector needs `ss` on Linux (from `iproute2`).

### Use the factory manually

Generate today's idea **proposal**:
```bash
python scripts/daily.py
```

Generate a runnable **text-statistics starter** with full docs:
```bash
python scripts/generate_project.py --slug text-stats-demo --name "Text Stats Demo"
python -m unittest discover -s projects/text-stats-demo/tests -v
```

The starter generator refuses to overwrite an existing project.

### Use GitHub Actions without installing anything

Open [Actions](https://github.com/3bHussein/Project-Factory-AI/actions). Choose **Daily proposal (review only)** or **Generate reviewed starter project**, then **Run workflow**. The latter needs a unique slug and a project name. Review the resulting PR; nothing is auto-merged.

The daily proposal workflow is scheduled at **07:15 UTC** (10:15 Egypt at UTC+3). GitHub may delay scheduled runs.

## 📚 Mandatory project documentation

Every project needs `README.md`, `ARCHITECTURE.md`, `INSTALLATION.md`, `USER-GUIDE.md`, `API.md`, `SECURITY.md`, `TEST-REPORT.md`, `CHANGELOG.md`, `DEVELOPMENT-LOG.md`, `HANDOVER.md` and tests. The automated validator checks file presence and minimum content, **not the factual accuracy** of the documents.

## Repository structure

- `projects/`: runnable tools, each with documentation and tests.
- `scripts/`: factory generator, daily proposals and validation.
- `ideas/backlog.json`: project ideas.
- `proposals/`: dated specifications, not runnable code.
- `automation-runs/`: proposal audit manifests.
- `.github/workflows/`: CI and automation.
- `dashboard/`: browser-based static guide.

More: [Automation Setup](docs/AUTOMATION-SETUP.md) · [Starter Workflow](docs/STARTER-WORKFLOW.md) · [Handover](HANDOVER.md).

**Safety:** no unapproved paid APIs, no writes to unrelated repositories, no auto-merge, and no secrets in source control.
