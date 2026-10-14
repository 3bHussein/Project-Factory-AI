# Architecture

`schedule / workflow_dispatch` → Python unit tests → `scripts/daily.py` → `proposals/YYYY-MM-DD/*.md` and `automation-runs/YYYY-MM-DD.json` → review pull request.

Input: `ideas/backlog.json` (unique slug identifiers).

No external AI agent, model key, hosting, or billing is configured. Future AI code generation is an explicitly separate phase.
