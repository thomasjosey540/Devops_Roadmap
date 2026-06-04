#!/usr/bin/python3
import os

userlist = ["alpha", "beta", "gama"]

print("Adding users to system")
print("#" * 72)

# Loop to add users from userlist
for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("User {} does not exist. Adding it".format(user))
        print("#" * 46)
        print()
        os.system("useradd {}".format(user))
    else:
        print("User already exists, skipping it")
        print("#" * 42)
        print()

# Check if group exists
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group does not exist. Adding it")
    print("#" * 46)
    print()
    os.system("groupadd science")
else:
    print("Group already exists, skipping it")
    print("#" * 42)
    print()

# Add users to science group
for user in userlist:
    print("Adding user {} to science group".format(user))
    print("#" * 46)
    print()
    os.system("usermod -G science {}".format(user))

# Create directory
print("Adding directory")
print("#" * 53)
print()

if os.path.isdir("/opt/science_dir"):
    print("Directory already exists, skipping it...")
else:
    os.mkdir("/opt/science_dir")

# Set ownership and permissions
print("Setting ownership and permissions on /opt/science_dir")
print("#" * 46)
print()
os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")