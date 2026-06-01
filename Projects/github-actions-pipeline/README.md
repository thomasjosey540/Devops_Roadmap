# GitHub Actions CI/CD Pipeline — Docker + AWS ECR

## Workflow Overview
Event-driven CI/CD pipeline using GitHub Actions for a Java web application.
Builds with Maven, scans with Trivy, containerizes with Docker, and pushes to AWS ECR.

## Triggers
| Trigger           | Description                           |
|-------------------|---------------------------------------|
| Push to main      | Runs full pipeline                    |
| Pull Request      | Runs Build, Testing, Security Scan    |
| workflow_dispatch | Manual trigger from GitHub UI         |
| Schedule          | Runs at 2:10 PM UTC, Monday to Friday |

## Jobs
| Job              | Depends On                        | Description                                  |
|------------------|-----------------------------------|----------------------------------------------|
| Build            | —                                 | Maven build, archives .war artifact          |
| Testing          | Build                             | Unit tests + Checkstyle (main branch only)   |
| Security_Scan    | Build                             | Trivy filesystem scan, uploads results       |
| BUILD_AND_DEPLOY | Build, Testing, Security_Scan     | Docker build + push to AWS ECR (main only)   |

## Key Concepts Used
- **needs:** — job dependency chaining
- **if: conditions** — branch-aware test execution
- **environment: production** — GitHub environment protection rules
- **artifacts** — passing .war files and scan results between jobs
- **secrets vs vars** — sensitive values in secrets, non-sensitive in vars

## GitHub Actions Variables Required
| Name                  | Type   | Description                     |
|-----------------------|--------|---------------------------------|
| AWS_ACCESS_KEY_ID     | Secret | AWS access key                  |
| AWS_SECRET_ACCESS_KEY | Secret | AWS secret key                  |
| AWS_REGION            | Var    | AWS region (e.g. us-east-1)     |
| ECR_REPOSITORY        | Var    | ECR repository name             |

Set secrets under:
Repository → Settings → Secrets and variables → Actions → Secrets

Set vars under:
Repository → Settings → Secrets and variables → Actions → Variables

## Source Project
Based on the vprofile-project application.