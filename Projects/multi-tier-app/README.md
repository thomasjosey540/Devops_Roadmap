# Multi-Tier Application Project

## 📌 Overview

This project demonstrates a multi-tier application infrastructure setup using multiple services.  
It was implemented using both manual configuration and automation via Vagrant.

---

## 🧱 Architecture

- Nginx → Web Server  
- Tomcat → Application Server  
- RabbitMQ → Message Broker  
- Memcached → Caching Layer  
- Elasticsearch → Search and Indexing Service  
- MySQL → Database  

---

## ⚙️ What I Did

### Manual Setup
- Created a virtual machine using Vagrant
- Installed services manually using Linux commands
- Started and verified each service using systemctl
- Tested services locally

### Automated Setup (Vagrant Provisioning)
- Defined infrastructure in Vagrantfile
- Automated installation of services
- Reduced manual setup effort
- Ensured repeatable environment setup

---

## 🛠️ Commands Used

vagrant up  
vagrant ssh  

sudo yum install httpd  
sudo systemctl start httpd  
systemctl status httpd  

---

## 🎯 Key Learning

- Understanding multi-tier architecture
- Linux service management
- Manual vs automated infrastructure setup
- Basics of provisioning in DevOps

---

## 📈 Outcome

Successfully created and managed a multi-service environment using both manual and automated approaches.