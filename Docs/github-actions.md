# GitHub Actions

## What is GitHub Actions?
A CI/CD platform built into GitHub. Workflows are defined as YAML files
and triggered by repository events like pushes, pull requests, or schedules.

## GitHub Actions vs Jenkins
| GitHub Actions               | Jenkins                         |
|------------------------------|---------------------------------|
| Built into GitHub            | Self-hosted server required     |
| YAML-based workflows         | Groovy-based Jenkinsfile        |
| GitHub-hosted runners        | Agents managed by you           |
| Free tier available          | Free but infra costs apply      |
| Marketplace actions          | Plugin ecosystem                |

## Core Concepts

### Workflow
- A YAML file in .github/workflows/
- Defines when to run (on:) and what to run (jobs:)

### Events (Triggers)
- push, pull_request, workflow_dispatch, schedule

### Jobs
- Independent units of work
- Run in parallel by default
- Use `needs:` to create dependencies

### Steps
- Sequential tasks within a job
- Can use `run:` for shell commands or `uses:` for actions

### Actions
- Reusable units from GitHub Marketplace
- Examples: actions/checkout, actions/upload-artifact,
  aws-actions/configure-aws-credentials

### Secrets & Variables
- Secrets: encrypted, for sensitive data (API keys, passwords)
- Variables: plain text, for non-sensitive config values

### Artifacts
- Files shared between jobs or saved after workflow completes
- Upload: actions/upload-artifact
- Download: actions/download-artifact

### Environments
- Named deployment targets (e.g. production)
- Can have protection rules, required reviewers, secrets

## Pipeline Flow in This Project
1. Push to main triggers workflow
2. Build job: Maven build, archives .war
3. Testing + Security Scan run in parallel (both need Build)
4. BUILD_AND_DEPLOY runs only after all three pass, only on main
5. Docker image built and pushed to AWS ECR, tagged with commit SHA