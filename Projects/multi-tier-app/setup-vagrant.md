# Vagrant Setup

## Objective

Automate multi-tier environment setup using Vagrant.

---

## Steps

1. Initialize Vagrant

vagrant init centos/7  

2. Start VM

vagrant up  

3. SSH into VM

vagrant ssh  

---

## Provisioning

Installed services using shell provisioning:

- Nginx
- Tomcat
- MySQL
- RabbitMQ
- Memcached

---

## Outcome

- Automated environment setup
- Reproducible infrastructure