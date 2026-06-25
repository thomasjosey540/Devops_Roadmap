# 🚀 DevOps Learning Journey

Hands-on DevOps learning and real-world infrastructure projects — documented section by section, from Linux fundamentals through CI/CD, Infrastructure as Code, configuration management, containers, and Kubernetes.

---

## 📌 Key Areas Covered

* DevOps fundamentals (CI/CD, delivery lifecycle)
* Linux system administration & server management
* Git version control
* Virtualization (VMs, Vagrant)
* Infrastructure provisioning & multi-VM setup
* Data formats (JSON, YAML) & scripting
* Networking fundamentals & troubleshooting
* Bash scripting & automation
* AWS cloud fundamentals & managed services (EC2, S3, RDS, ELB, Beanstalk, CloudFront)
* CI/CD pipelines (Jenkins, GitHub Actions, GitLab CI)
* Infrastructure as Code (Terraform)
* Configuration management (Ansible)
* Containerization (Docker, Docker Compose, multi-service apps)
* Container orchestration (Kubernetes, Helm, EKS via Terraform)

---

## 🛠 Tech Stack

**CI/CD:** Jenkins · GitHub Actions · GitLab CI · Maven
**Containers & Orchestration:** Docker · Docker Compose · Kubernetes · Helm · kubectl · AWS ECR · AWS ECS
**IaC & Config Management:** Terraform · Ansible
**Cloud (AWS):** EC2 · S3 · RDS · ELB · Auto Scaling · IAM · Elastic Beanstalk · ElastiCache · CloudFront · Route 53
**Quality & Security:** SonarQube · Trivy · Nexus Repository Manager
**Languages & Scripting:** Python · Bash · Boto3 · Fabric
**OS & Tooling:** Linux (Ubuntu / CentOS) · Git · VirtualBox · Vagrant · Apache · Lens

---

## 📂 Repository Structure

* `Docs/` → Concepts and notes
* `Labs/` → Hands-on practice
* `Projects/` → Real-world implementations
* `Scripts/` → Automation scripts

---

## 🎯 Objective

To build deep, hands-on DevOps & Cloud skills through real projects — CI/CD pipelines, Infrastructure as Code, configuration management, containerization, and Kubernetes orchestration — documented openly as I learn.

---

## 🚀 Projects

### CI/CD Pipelines
* **Jenkins** — Pipeline as Code: Maven build, SonarQube quality gate, Docker image, push to AWS ECR
* **GitHub Actions** — parallel build/test/Trivy scan, Docker + AWS ECR
* **GitLab CI** — multi-stage pipeline with Docker-in-Docker and GitLab Container Registry
📂 `Projects/`

### Infrastructure as Code — Terraform
AWS EC2 provisioning with security groups, remote state (S3), and provisioners.
📂 `Projects/terraform-aws-ec2`

### Configuration Management — Ansible
Playbooks, roles, Jinja2 templates, handlers, and AWS provisioning.
📂 `Projects/ansible-configuration-management`

### Containerization — Docker
Multi-stage Dockerfiles, volumes, Docker Compose, and a fully containerized multi-service microservice app.
📂 `Projects/docker-containerization` · `Projects/microservice-containerization`

### Orchestration — Kubernetes
Deployments, Services, Ingress, ConfigMaps/Secrets, Helm charts, and an EKS cluster provisioned with Terraform.
📂 `Projects/kubernetes-orchestration`

### Multi-Tier Application
Nginx · Tomcat · RabbitMQ · Memcached · Elasticsearch · MySQL — manual and Vagrant-automated setup.
📂 `Projects/multi-tier-app`

---

## ⚙️ Scripts

### System Monitoring Script
Displays system information (date, uptime, memory, disk usage); demonstrates Bash automation.
📂 `Scripts/system-monitor.sh`

---

## 📈 Current Progress

* ✅ DevOps fundamentals
* ✅ Environment setup
* ✅ Virtualization (Vagrant)
* ✅ Linux fundamentals & server setup
* ✅ Git basics
* ✅ Provisioning & multi-VM setup
* ✅ JSON, YAML & scripting
* ✅ Networking fundamentals
* ✅ Bash scripting & automation
* ✅ AWS fundamentals & cloud services
* ✅ Multi-tier deployment on AWS
* ✅ Application refactoring using AWS managed services
* ✅ CI/CD with Jenkins
* ✅ CI/CD with GitHub Actions
* ✅ CI/CD with GitLab
* ✅ Python for DevOps (OS automation, Fabric, Boto3)
* ✅ Terraform (Infrastructure as Code)
* ✅ Ansible (configuration management)
* ✅ Docker
* ✅ Containerization (multi-service apps)
* ✅ Kubernetes (orchestration, Helm, EKS via Terraform)
* ✅ K8s App Deployment (VProfile on Kops)
* 🔜 GitOps project