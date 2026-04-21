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


---

## Vagrant for Server Setup

Vagrant can be used to create and configure servers.

### Basic Workflow

vagrant init centos/7  
vagrant up  
vagrant ssh  

---

## Provisioning

Provisioning allows automatic setup of the VM.

Example:

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: <<-SHELL
    sudo yum install -y httpd
    sudo systemctl start httpd
  SHELL
end

---

## Manual vs Automatic Setup

Manual:
- Install httpd manually
- Start service manually

Automatic:
- Defined in Vagrantfile
- Runs during `vagrant up`

---

## Multi-VM Setup

Example:

Vagrant.configure("2") do |config|

  config.vm.define "web" do |web|
    web.vm.box = "centos/7"
  end

  config.vm.define "db" do |db|
    db.vm.box = "centos/7"
  end

end

---

## Key Learning

- Infrastructure can be automated
- Vagrant simplifies server setup
- Multi-VM simulates real environments