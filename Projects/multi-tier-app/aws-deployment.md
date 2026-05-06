# AWS Deployment - Multi Tier Application

## Overview

Deployed a multi-tier application on AWS using scalable and highly available infrastructure.

---

## Architecture

- Web Layer: Nginx
- Application Layer: Tomcat
- Messaging: RabbitMQ
- Caching: Memcached
- Database: MySQL

---

## AWS Services Used

- EC2 → Application hosting
- Security Groups → Access control
- Key Pairs → SSH authentication
- Elastic Load Balancer → Traffic distribution
- Auto Scaling Group → Scaling instances
- Route 53 → DNS management

---

## Steps Performed

### 1. Infrastructure Setup
- Created EC2 instances
- Configured security groups
- Connected using key pairs

### 2. Application Setup
- Installed required services (Nginx, Tomcat, MySQL, etc.)
- Deployed application artifacts

### 3. Load Balancer
- Configured ELB for traffic distribution

### 4. Auto Scaling
- Created launch configuration
- Configured auto scaling group

### 5. DNS Setup
- Configured Route 53 for domain routing

---

## Outcome

- Successfully deployed multi-tier application on AWS
- Achieved scalability using Auto Scaling
- Implemented high availability using Load Balancer