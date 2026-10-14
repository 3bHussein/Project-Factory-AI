# Request a custom project

Use **[New issue](https://github.com/3bHussein/Project-Factory-AI/issues/new/choose)** and select **Request a custom project**.

Write a clear name, problem, platform, desired features, sample input/output, constraints, and acceptance criteria. For example: "Log Analyzer Pro; parse local nginx logs; group 4xx/5xx; produce offline HTML report; test with sample logs."

## What happens today

1. A GitHub Issue records the idea for human review. A GitHub Actions workflow automatically opens a **specification-only pull request** for a correctly titled request after this automation is merged.
2. A developer (or a coding agent explicitly given this task) implements a real project in a feature branch.
3. CI runs tests, documentation checks and supported-platform checks.
4. A PR is reviewed and merged before the dashboard lists it as available.

**Important:** Opening an issue **does not currently trigger automatic custom code generation**. The manual starter workflow generates only the fixed text-statistics template. There is no general-purpose AI coding worker, and no paid AI service has been configured. Do not promise automatic delivery of a custom issue.

## Good project acceptance checklist

- Real working code, not a renamed demo
- README, architecture, installation, user guide, CLI/API, security, test report, changelog, development log, handover
- Tests for success, invalid input and failure conditions
- Safe defaults, no secrets or destructive operations
- Human review before merge

For existing supported workflows see [Starter Workflow](STARTER-WORKFLOW.md).
