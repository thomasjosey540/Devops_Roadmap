#!/usr/bin/python3
from fabric.api import *

env.user = 'devops'

def greeting(msg):
    """Print a greeting message"""
    print("Good {}".format(msg))

def system_info():
    """Display local system information"""
    print("Disk Space")
    local("df -h")
    print("RAM size")
    local("free -m")
    print("System uptime")
    local("uptime")

def remote_exec():
    """Execute commands on remote server"""
    print("Get System Info")
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")
    sudo("yum install mariadb-server -y")
    sudo("systemctl start mariadb")
    sudo("systemctl enable mariadb")

def web_setup(WEBURL, DIRNAME):
    """Download and deploy website to remote webservers"""
    print("#" * 83)
    local("apt install zip unzip -y")
    print("#" * 83)
    print("Installing dependencies")
    print("#" * 83)
    sudo("yum install httpd wget unzip -y")
    print("#" * 83)
    print("Start and enable service")
    print("#" * 83)
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    print("#" * 83)
    print("Downloading and pushing website to webservers")
    print("#" * 83)
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip -o website.zip")
    print("#" * 83)
    with lcd(DIRNAME):
        local("zip -r tooplate.zip *")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)
    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")
    sudo("systemctl restart httpd")
    print("Website setup is done.")