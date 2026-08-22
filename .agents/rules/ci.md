---
trigger: glob
description: CI least privilege, pinned Actions, and dependency update policy
globs:
  - "**/.github/workflows/*.yml"
  - "**/.github/workflows/*.yaml"
  - "**/.github/dependabot.yml"
  - "**/.gitlab-ci.yml"
  - "**/azure-pipelines*.yml"
  - "**/Jenkinsfile"
---

@../../rules/ci.md
