# Automation setup and operating policy

## What is already automatic
The daily GitHub Actions workflow runs at 07:15 UTC and on manual dispatch. It selects a backlog idea, writes a specification and run manifest, and opens a review-only pull request. GitHub Actions schedules can be delayed. The daily workflow does **not** generate application source code or full project documentation yet.

## Enable automation
1. Repository > Settings > Actions > General: allow Actions, choose appropriate workflow permissions and enable PR creation for GitHub Actions.
2. Repository > Actions > Daily proposal (review only) > Run workflow to smoke-test.
3. Inspect the new proposal PR, run manifest and job logs. Review before merging.
4. Configure branch protection/rulesets for main, requiring the quality gate and human review where available.
5. Keep GitHub Actions secrets out of commits and log output. Never enable a paid API without explicit approval.

## Production-ready future architecture
A bounded generation agent would take a project specification, generate a real runnable application, include all required docs, test in an isolated runner, run security and quality gates, then create a review-only PR. This agent is **not implemented** and no AI credentials have been added.

## Required project documentation
Every project needs README.md, ARCHITECTURE.md, INSTALLATION.md, USER-GUIDE.md, API.md (state 'not applicable' where appropriate), SECURITY.md, TEST-REPORT.md, CHANGELOG.md, DEVELOPMENT-LOG.md, HANDOVER.md, and automated tests. Documentation must contain real project-specific details; automated structural validation is only a minimum.

## Troubleshooting
If PR creation fails with 'not permitted', enable 'Allow GitHub Actions to create and approve pull requests' in Settings > Actions > General. For other failures, check Actions run logs and record findings in DEVELOPMENT-LOG.md.

## Human control
No auto-merge, no unapproved billing, no writes to existing external repositories, no unsafe deletion, and no secret publication.
