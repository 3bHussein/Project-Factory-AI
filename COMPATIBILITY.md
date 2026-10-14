# Compatibility and Safety

- No integration with `ProgressXX` or any other existing project.
- Default branch main is not modified by generation jobs; changes go through PRs.
- Never rewrite historical commits or force-push.
- No automatic deletion, cleanup or system repair in tool projects.
- Pin/assess third-party actions before production; audit workflow permissions.
- Merge may still cause mistakes; use tests and human code review.
