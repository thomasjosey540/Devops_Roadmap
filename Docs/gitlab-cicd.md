# GitLab CI/CD

## What is GitLab CI/CD?
A built-in CI/CD platform in GitLab. Pipelines are defined in a
.gitlab-ci.yml file at the root of the repository and triggered
by repository events.

## Pipeline Structure
- **stages** — ordered list of phases (build, test, deploy)
- **jobs** — individual units of work assigned to a stage
- **script** — shell commands the job runs
- **image** — Docker image the job runs inside

## Key Keywords

### rules
Controls when a job runs. Replaces older only/except syntax.
```yaml
rules:
  - if: '$CI_COMMIT_BRANCH == "main"'
  - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  - when: never
```

### needs
Creates job dependencies and enables artifact passing.
```yaml
needs:
  - job: build-job
    artifacts: true
```

### artifacts
Files saved and passed between jobs or downloaded after pipeline.
```yaml
artifacts:
  paths:
    - target/
  expire_in: 1 hour
```

### cache
Files persisted across pipeline runs to speed up jobs.
```yaml
cache:
  paths:
    - .m2/repository
```

## GitLab vs GitHub Actions vs Jenkins

| Feature              | GitLab CI        | GitHub Actions     | Jenkins             |
|----------------------|------------------|--------------------|---------------------|
| Config file          | .gitlab-ci.yml   | .github/workflows/ | Jenkinsfile         |
| Runner               | GitLab Runner    | GitHub Runner      | Jenkins Agent       |
| Container Registry   | Built-in         | External needed    | External needed     |
| Trigger syntax       | rules:           | if: conditions     | when conditions     |
| Self-hosted runner   | Yes              | Yes                | Yes (required)      |
| Free tier            | Yes              | Yes                | Free, infra costs   |

## Docker-in-Docker (dind)
Used when the CI job itself needs to run Docker commands.
Requires the docker:dind service and disabling TLS for simplicity.

## GitLab Predefined CI Variables
GitLab automatically injects variables like CI_COMMIT_SHA,
CI_REGISTRY, CI_REGISTRY_USER, CI_REGISTRY_PASSWORD into every
pipeline — no manual secret setup needed for registry operations.

## Pipeline Flow in This Project
1. Push to main/develop triggers pipeline
2. build-job: Maven build, archives target/
3. test-job and security-scan run in parallel (both need build-job)
4. docker-build-publish runs after test + security pass
5. Image pushed to GitLab registry tagged with commit SHA + latest
6. notify-on-failure runs only if any stage fails