# GitLab CI/CD Setup Notes

## How GitLab CI Works
- Pipeline defined in .gitlab-ci.yml at root of repo
- Triggered by push, merge request, schedule, or manual web trigger
- Jobs run on GitLab Runners (shared or self-hosted)
- Stages run sequentially, jobs within a stage run in parallel

## Key Concepts

### Stages
- Defined at top of .gitlab-ci.yml
- Jobs assigned to stages via `stage:` keyword
- If any job fails, subsequent stages are skipped

### needs
- Allows jobs to depend on specific other jobs
- Can pass artifacts between jobs with `artifacts: true`
- Skips waiting for entire stage to complete

### rules
- Controls when a job runs
- Replaces older `only/except` syntax
- Supports branch names, pipeline sources, variables

### Cache vs Artifacts
- Cache: persisted between pipeline runs (Maven repo, Trivy cache)
- Artifacts: passed between jobs within same pipeline (target/, reports)

### Docker-in-Docker (dind)
- Allows Docker commands inside a CI job
- Requires docker:dind service
- TLS disabled for simplicity: DOCKER_TLS_CERTDIR: ""

## GitLab Container Registry
- Built into every GitLab project
- No external registry setup needed
- Authenticated automatically via CI_REGISTRY_* variables

## GitLab CI vs GitHub Actions
| GitLab CI                    | GitHub Actions                  |
|------------------------------|---------------------------------|
| .gitlab-ci.yml               | .github/workflows/*.yml         |
| Stages + Jobs                | Jobs + Steps                    |
| needs: for dependencies      | needs: for dependencies         |
| Built-in Container Registry  | Requires external registry      |
| GitLab Runners               | GitHub-hosted Runners           |
| rules: for conditions        | if: for conditions              |