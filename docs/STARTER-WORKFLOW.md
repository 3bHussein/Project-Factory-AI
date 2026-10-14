# Generate a documented starter from GitHub Actions

1. Open Actions > Generate reviewed starter project > Run workflow.
2. Enter a **new** lowercase slug such as `text-counter-demo` and a project name.
3. GitHub Actions creates the reviewed offline text-statistics Python template, ten documentation files and tests.
4. The workflow validates documentation and executes the generated project's tests.
5. If checks succeed, it opens a pull request for **human review**. No auto-merge.

## Limitations
This workflow is **manual dispatch**, not daily automatic source-code generation. The existing daily workflow still creates idea specifications only. Every generated starter is the same text-statistics functionality, so do not create renamed duplicates and call them distinct useful tools. Different reviewed templates and idea-to-template matching must be implemented before automated daily production of varied projects.

## Costs and safety
No AI API, secrets, external repository write, or paid service is used. A duplicate slug causes the job to fail rather than overwrite a project. GitHub Actions usage remains subject to GitHub plan limits.
