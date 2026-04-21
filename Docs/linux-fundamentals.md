# Linux Fundamentals

## File System

- / → root
- /home → user directories
- /etc → configuration
- /var → logs

---

## Basic Commands

pwd → print working directory  
ls → list files  
cd → change directory  

touch file.txt  
cp file1 file2  
mv file1 file2  
rm file.txt  

---

## Vim Editor

vim file.txt  
i → insert mode  
esc → normal mode  
:wq → save and exit  

---

## Users & Permissions

whoami  
id  

chmod 755 file.sh  
chown user file.txt  

---

## Processes & Services

ps aux  
top  
kill -9 PID  

systemctl start nginx  
systemctl status nginx  

---

## Package Management

sudo apt update  
sudo apt install git  

---

## Filters & Redirection

cat file.txt  
grep "error" file.txt  

echo "hello" > file.txt  
echo "world" >> file.txt  

---

## Archiving

tar -cvf file.tar folder/  
tar -xvf file.tar  

---

## Linux Server (Apache - httpd)

Install:
sudo yum install httpd

Start:
sudo systemctl start httpd

Check:
systemctl status httpd

Enable on boot:
sudo systemctl enable httpd

Test:
curl localhost

---

## Key Learning

- Linux servers run services
- Apache (httpd) is a web server
- Services must be managed using systemctl