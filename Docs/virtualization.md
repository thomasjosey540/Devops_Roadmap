# Virtualization

## Overview

Virtualization allows multiple operating systems to run on a single physical machine.

---

## Manual VM Setup

Tools:
- VirtualBox / VMware

Steps:
- Install hypervisor
- Load OS ISO
- Allocate CPU, RAM, disk

---

## Vagrant

Vagrant automates virtual machine provisioning.

Commands:
vagrant init ubuntu/bionic64
vagrant up
vagrant ssh

---

## Benefits

- Reproducible environments
- Faster setup
- Useful for DevOps workflows