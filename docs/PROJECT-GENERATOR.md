# Project Generator V1

This is a **free deterministic template generator**, not an AI coding agent. It produces a runnable, offline text statistics Python CLI, its tests, and all ten mandatory documentation files. The project name and slug are customizable, but its actual functionality is the same reviewed text-statistics template. Do not present a renamed generated project as a new tool with different capabilities.

## Generate a starter project
```bash
python scripts/generate_project.py --slug text-statistics --name "Text Statistics"
python -m unittest discover -s projects/text-statistics/tests -v
python scripts/validate_projects.py
```

The generator refuses to overwrite existing non-empty project directories. It does not push or merge anything automatically.

## Next phase
Add separate reviewed templates for different useful tool categories; then build an opt-in AI agent with sandboxed execution, explicit budget caps, security reviews and PR-only delivery. Avoid producing superficial renamed duplicates.
