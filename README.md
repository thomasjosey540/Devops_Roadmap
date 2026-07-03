# 🚀 DevOps Learning Journey

Hands-on DevOps learning and real-world infrastructure projects — documented section by section, from Linux fundamentals through CI/CD, Infrastructure as Code, configuration management, containers, Kubernetes, and a full GitOps capstone.

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
* GitOps (Argo CD continuous delivery to EKS)

---

## 🛠 Tech Stack

**CI/CD:** Jenkins · GitHub Actions · GitLab CI · Maven
**Containers & Orchestration:** Docker · Docker Compose · Kubernetes · Helm · kubectl · AWS ECR · AWS ECS
**GitOps:** Argo CD
**IaC & Config Management:** Terraform · Ansible
**Cloud (AWS):** EC2 · S3 · RDS · ELB · Auto Scaling · IAM · EKS · Elastic Beanstalk · ElastiCache · CloudFront · Route 53
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

To build deep, hands-on DevOps & Cloud skills through real projects — CI/CD pipelines, Infrastructure as Code, configuration management, containerization, Kubernetes orchestration, and GitOps — documented openly as I learn.

---

## 🚀 Projects

### ⭐ GitOps Capstone — CI/CD + Argo CD + EKS (Terraform + Helm)
End-to-end GitOps pipeline for the VProfile app: **GitHub Actions** builds, tests, SonarQube-scans, and pushes the image to **AWS ECR**; the CI job updates the **Helm** chart in Git; **Argo CD** syncs it to an **Amazon EKS** cluster provisioned with **Terraform**. Git is the single source of truth.

* **[vprofile-app-public](https://github.com/thomasjosey540/vprofile-app-public)** — application + GitHub Actions CI/CD
* **[vprofile-helm-public](https://github.com/thomasjosey540/vprofile-helm-public)** — Helm chart (synced by Argo CD)
* **[vprofile-infra-public](https://github.com/thomasjosey540/vprofile-infra-public)** — Terraform (EKS) + Argo CD

### Kubernetes App Deployment — VProfile Multi-Tier App
Deployed the VProfile multi-tier app (Tomcat, MySQL, Memcached, RabbitMQ) to a **Kops-provisioned Kubernetes cluster on AWS**, with a PersistentVolumeClaim, Secrets, init-container ordering, Services, and Nginx Ingress.
📂 `Projects/kubernetes-app-deployment`

### Orchestration — Kubernetes
Deployments, Services, Ingress, ConfigMaps/Secrets, Helm charts, and an EKS cluster provisioned with Terraform.
📂 `Projects/kubernetes-orchestration`

### Containerization — Docker
Multi-stage Dockerfiles, volumes, Docker Compose, and a fully containerized multi-service microservice app.
📂 `Projects/docker-containerization` · `Projects/microservice-containerization`

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
* ✅ GitOps Capstone (CI/CD → Argo CD → EKS)

