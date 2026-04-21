# Linux Practice Labs

## Objective

Practice core Linux commands in a real terminal environment.

---

## Lab 1: Navigation

pwd  
ls -la  
cd /etc  

---

## Lab 2: File Operations

touch test.txt  
echo "DevOps" > test.txt  
cat test.txt  

---

## Lab 3: Process Monitoring

ps aux  
top  

---

## Lab 4: Permissions

chmod 755 test.txt  

---

## Outcome

- Gained hands-on experience with Linux commands
- Understood system navigation and file handling
- Practiced process monitoring and permissions

---

## Lab 5: Git Practice

Initialize repo:
git init

Add files:
git add .

Commit:
git commit -m "first commit"

Check log:
git log

Push to remote:
git push origin main


---

## Lab: Apache Server Setup

sudo yum install httpd  
sudo systemctl start httpd  
systemctl status httpd  
curl localhost  

---

## Lab: Vagrant Provisioning

Create VM:
vagrant init centos/7  
vagrant up  
vagrant ssh  

Inside VM:
sudo yum install httpd  
sudo systemctl start httpd  

---

## Lab: Multi-VM

vagrant up  

Check:
vagrant status  

Connect:
vagrant ssh web  
vagrant ssh db  

---

## Outcome

- Set up web server using Apache
- Automated setup using Vagrant provisioning
- Created multi-VM environment