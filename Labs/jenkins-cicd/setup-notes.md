# Jenkins CI/CD Setup Notes

## Infrastructure
- Jenkins server: EC2 instance
- SonarQube server: EC2 instance
- Nexus server: EC2 instance

## Jenkins Setup
- Installed plugins: Git, Maven Integration, Docker Pipeline,
  SonarQube Scanner, Nexus Artifact Uploader, Slack Notification
- Configured JDK 17 and Maven 3.9 under Global Tool Configuration
- Added AWS credentials under Jenkins Credentials Manager

## SonarQube Setup
- Integrated with Jenkins via SonarQube Scanner plugin
- Created Quality Gate and linked to project
- Webhook configured to notify Jenkins of gate result

## Nexus Setup
- Used as artifact repository for .war files
- Configured in pipeline via PAAC (Pipeline as a Code)

## Docker + ECR Setup
- Docker installed on Jenkins agent
- ECR repository created in AWS
- Pipeline builds image, tags with build number, pushes to ECR

## ECS Setup
- ECS cluster created to pull and run image from ECR

