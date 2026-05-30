# CI/CD with Jenkins

## What is CI/CD?
- **Continuous Integration (CI):** Automatically build and test code on every commit
- **Continuous Delivery (CD):** Automatically deliver tested code to a target environment

## Freestyle vs Pipeline as Code
| Freestyle        | Pipeline as Code (Jenkinsfile)      |
|------------------|-------------------------------------|
| GUI-based        | Code-based (Groovy DSL)             |
| Hard to version  | Stored in Git alongside source code |
| Limited reuse    | Reusable, shareable, reviewable     |
| Simple jobs only | Handles complex multi-stage flows   |

## Jenkins Architecture
- **Master:** Schedules jobs, monitors agents, serves UI
- **Agent:** Executes the actual build steps
- **Executor:** A slot on an agent for running a job

## Key Concepts

### Build Triggers
- Poll SCM: Jenkins checks Git on a schedule
- Webhook: Git notifies Jenkins on push (preferred)
- Manual: Triggered by user

### Plugins Used
- Git Plugin
- Maven Integration
- Docker Pipeline
- SonarQube Scanner
- Nexus Artifact Uploader
- Slack Notification

## Code Quality Tools

### SonarQube
- Performs static code analysis
- Checks for bugs, vulnerabilities, code smells
- Quality Gate: pass/fail threshold that can abort the pipeline

### Checkstyle
- Enforces Java code style standards
- Run via Maven: `mvn checkstyle:checkstyle`

## Artifact Management — Nexus
- Stores build artifacts (.war, .jar files)
- Acts as a central repository for versioned builds
- Prevents rebuilding the same artifact multiple times

## Docker CI/CD Flow
1. Code pushed to GitHub
2. Jenkins fetches code
3. Maven builds .war file
4. Checkstyle + SonarQube analysis runs
5. Quality Gate evaluated — pipeline aborts if failed
6. Docker image built using multistage Dockerfile
7. Image pushed to AWS ECR (tagged with build number + latest)
8. Local images cleaned up from agent

## Key Decisions in This Pipeline
- Multistage Dockerfile keeps production image small
- Quality Gate set to abort — enforces code quality as hard requirement
- Build number tagging on ECR enables rollback by build ID
- Image cleanup stage prevents disk exhaustion on Jenkins agent
- All credentials stored in Jenkins, never in code