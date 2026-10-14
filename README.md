# Project Factory AI

Free-first project proposal factory covering Web, Windows, Linux and cross-platform tools.

**Current capability:** generates dated project *specifications*, not implemented application code. Each daily run proposes changes via a pull request for human review. No auto-merge, deployment or paid AI API.

## Start
```bash
python -m unittest discover -s tests -v
python scripts/daily.py
```

Daily schedule: 07:15 UTC (10:15 Egypt, UTC+3). GitHub scheduled runs are not guaranteed to fire at the exact minute.

## Continuity
Read HANDOVER.md, PROJECT-STATE.md, DEVELOPMENT-LOG.md, TEST-REPORT.md, and open GitHub PRs before making changes. Never edit unrelated repositories.

## Safeguards
- Main is updated by human-reviewed PR only.
- Destructive utilities require explicit confirmation and dry-run.
- Standard-library Python for proposal generator.
- Paid services prohibited until separately approved.
- Actual AI implementation agent not configured in V3.
