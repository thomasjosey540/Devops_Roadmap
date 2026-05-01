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


---

## Lab: JSON Practice

Create a JSON file:

{
  "app": "web",
  "port": 80
}

---

## Lab: YAML Practice

Create a YAML file:

app: web
port: 80

---

## Lab: Python Basics

x = 10
name = "devops"

print(x)
print(name)

---

## Outcome

- Practiced JSON and YAML formats
- Understood basic Python variables
- Learned how data is structured in DevOps


---

## Networking Lab

Check IP:
ifconfig  

Ping:
ping google.com  

Trace route:
traceroute google.com  

Check connections:
netstat -antp  

Scan ports:
nmap localhost  

DNS lookup:
dig google.com  

Routing table:
route -n  

ARP table:
arp -a  

Network diagnostics:
mtr google.com  

Test port:
telnet google.com 80  

---

## Outcome

- Practiced networking commands  
- Learned how to debug connectivity issues  
- Understood how services communicate over network  

---

## Docker Basic Lab

Check Docker version:
docker --version  

Run test container:
docker run hello-world  

List containers:
docker ps  

List images:
docker images  

---

## Outcome

- Ran first Docker container  
- Understood basic Docker commands  



---

## Bash Scripting Lab

Print message:
echo "Hello"

Variables:
name="devops"
echo $name

User input:
read name
echo $name

If condition:
if [ 5 -eq 5 ]
then
  echo "Equal"
fi

Loop:
for i in 1 2 3
do
  echo $i
done

---

## Outcome

- Practiced bash scripting basics  
- Learned automation using scripts  