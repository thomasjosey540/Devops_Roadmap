# GitLab CI/CD Pipeline — Docker + GitLab Container Registry

## Pipeline Overview
Event-driven CI/CD pipeline using GitLab CI for a Java web application.
Builds with Maven, tests with JUnit + Checkstyle, scans with Trivy,
containerizes with Docker, and pushes to GitLab Container Registry.

## Pipeline Stages
| Stage    | Job                   | Description                                        |
|----------|-----------------------|----------------------------------------------------|
| build    | build-job             | Maven build, archives target/ as artifact          |
| test     | test-job              | Unit tests + Checkstyle analysis                   |
| security | security-scan         | Trivy filesystem scan, uploads results             |
| docker   | docker-build-publish  | Docker build + push to GitLab registry             |
| notify   | notify-on-failure     | Echoes failure message if any stage fails          |

## Triggers
| Trigger               | Description                              |
|-----------------------|------------------------------------------|
| Push to main/develop  | Runs full pipeline                       |
| Merge Request         | Runs full pipeline                       |
| Web (manual)          | Triggered from GitLab UI                 |
| Schedule              | Triggered on defined schedule            |

## Key Concepts Used
- **stages** — defines execution order
- **needs** — job dependency and artifact passing between jobs
- **rules** — branch and event-based job control
- **cache** — Maven and Trivy cache across pipeline runs
- **artifacts** — passing target/ and scan results between stages
- **docker:dind** — Docker-in-Docker for building images inside CI
- **CI_REGISTRY_*** — GitLab predefined variables for registry auth

## GitLab Predefined Variables Used
| Variable            | Description                              |
|---------------------|------------------------------------------|
| CI_COMMIT_SHA       | Commit SHA used as image tag             |
| CI_REGISTRY         | GitLab Container Registry URL            |
| CI_REGISTRY_USER    | Registry login username                  |
| CI_REGISTRY_PASSWORD| Registry login password                  |
| CI_REGISTRY_IMAGE   | Full image path in registry              |
| CI_COMMIT_BRANCH    | Current branch name                      |
| CI_PIPELINE_SOURCE  | What triggered the pipeline              |

No manual secrets needed — all registry variables are
provided automatically by GitLab CI.

## Source Project
Based on the vprofile-project application.