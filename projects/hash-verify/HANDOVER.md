# Handover

Review README.md, ARCHITECTURE.md, SECURITY.md and TEST-REPORT.md before changes. Run `python -m unittest discover -s projects/hash-verify/tests -v` from repo root. Verify CLI manually on a known test file and compare against `sha256sum` or a trusted published checksum. Keep the program offline and read-only. Update CHANGELOG.md and DEVELOPMENT-LOG.md after changes; do not merge with failing CI.
