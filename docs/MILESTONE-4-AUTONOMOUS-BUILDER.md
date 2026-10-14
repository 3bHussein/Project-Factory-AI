# Milestone 4 — Autonomous Project Builder

## Goal
Submit a project idea from the dashboard and track its progress through specification, implementation, automated testing, and human-reviewed pull request without returning to chat.

## Current working stages
1. Browser builder prepares a structured request locally.
2. User explicitly confirms creation of a GitHub Issue.
3. GitHub Actions converts matching issues into specification-only PRs.
4. CI validates existing projects on supported platforms.

## Missing capabilities (not yet operational)
- Authenticated one-click request submission inside the dashboard (no browser-stored GitHub token).
- Secure coding agent that interprets arbitrary specifications and writes distinct runnable code.
- Sandboxed execution, network and secret isolation, spending limits, and bounded retry policy.
- Real-time project status in dashboard.
- End-to-end tests of issue -> spec PR -> implementation PR -> CI -> review.

## Agent execution contract
- Source: approved project request and immutable issue number.
- Scope: only this repository; never other repositories.
- Output: new project directory, ten docs, automated tests, implementation PR.
- Safety: no secret access from untrusted issue text, no shell interpolation of issue content, no auto-merge, no deployment or paid service without explicit approval.
- Quality: platform-specific CI, input validation, security checks, and manual approval.
- Failure: show failed/blocked state with actionable logs; do not falsely claim a project is built.

## Provider decision gate
A general coding model or agent runner is required to implement arbitrary natural-language projects. GitHub Actions is an executor, **not** an AI model. No model provider or paid API has been enabled. Choose an authorized provider and its funding/security model before enabling coding automation.

## Definition of done
A fresh issue submitted from the builder results in a genuinely distinct runnable application, validated tests, and a reviewable PR without chat intervention. A specification-only PR does not satisfy this milestone.
