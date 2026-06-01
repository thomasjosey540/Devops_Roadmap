# GitHub Actions Setup Notes

## How GitHub Actions Works
- Workflows are YAML files stored in .github/workflows/
- Triggered by events: push, pull_request, schedule, workflow_dispatch
- Jobs run on GitHub-hosted runners (ubuntu-latest)
- Jobs run in parallel by default, use `needs:` for sequencing

## Key Concepts

### Triggers
- push/pull_request: event-based
- workflow_dispatch: manual trigger from GitHub UI
- schedule: cron syntax (UTC timezone)

### Jobs vs Steps
- Jobs: independent units, run in parallel unless `needs:` is set
- Steps: sequential actions within a job

### Artifacts
- Upload: actions/upload-artifact@v4
- Download: actions/download-artifact@v4
- Used to pass .war files and scan results between jobs

### Conditions
- `if: github.ref == 'refs/heads/main'` — only run on main branch
- `if: failure()` — only run if previous step failed

### Secrets vs Variables
- Secrets: sensitive values (AWS keys), encrypted, not visible in logs
- Variables: non-sensitive config (region, repo name), visible in logs

## Security Scan — Trivy
- Scans filesystem for vulnerabilities in OS packages and libraries
- exit-code: 0 means pipeline does not fail on findings (informational)
- Results uploaded as artifact for review

## AWS Integration
- aws-actions/configure-aws-credentials@v1 — sets up AWS CLI auth
- aws-actions/amazon-ecr-login@v1 — authenticates Docker to ECR
- Image tagged with github.sha for full traceability

