# Manual Setup

## Steps

### 1. Install Services

sudo yum install nginx  
sudo yum install tomcat  
sudo yum install mysql-server  
sudo yum install rabbitmq-server  
sudo yum install memcached  

---

### 2. Start Services

sudo systemctl start nginx  
sudo systemctl start tomcat  
sudo systemctl start mysqld  
sudo systemctl start rabbitmq-server  
sudo systemctl start memcached  

---

### 3. Deploy Application

- Build application artifact
- Place in Tomcat webapps directory

---

## Outcome

- Successfully configured multi-tier application manually