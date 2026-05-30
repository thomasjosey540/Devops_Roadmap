# Jenkins CI/CD Pipeline — Docker + AWS ECS

## Pipeline Overview
End-to-end CI/CD pipeline for a Java web application built with Maven,
analyzed with SonarQube, containerized with Docker, and pushed to AWS ECR.

## Pipeline Stages
| Stage                   | Description                                               |
|-------------------------|-----------------------------------------------------------|
| Fetch Code              | Pulls from GitHub (docker branch)                         |
| Build                   | Maven build, archives .war artifact                       |
| Unit Test               | Runs Maven test suite                                     |
| Checkstyle Analysis     | Static code style check                                   |
| Sonar Code Analysis     | SonarQube scan (quality metrics)                          |
| Quality Gate            | Aborts pipeline if quality gate fails                     |
| Build App Image         | Builds Docker image (multistage Dockerfile)               |
| Upload App Image        | Pushes image to AWS ECR (tagged by build number + latest) |
| Remove Container Images | Cleans up local Docker images on agent                    |

## Tools Used
- Jenkins
- Maven 3.9 / JDK 17
- SonarQube 8.0
- Nexus Repository Manager
- Docker
- AWS ECR
- AWS ECS

## Jenkins Environment Variables Required
| Variable       | Description                       |
|----------------|-----------------------------------|
| AWS_ACCOUNT_ID | Your AWS account ID               |
| AWS_REGION     | AWS region (e.g. us-east-1)       |
| awscreds       | AWS credentials stored in Jenkins |

Set these under:
Jenkins → Manage Jenkins → Configure System → Global Properties → Environment Variables

## Source Project
Based on the vprofile-project application.