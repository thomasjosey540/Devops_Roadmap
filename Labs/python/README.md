# Python Labs

## Scripts

### check-file.py
Checks whether a given path is a file, directory, or does not exist.
Uses the `os` module for filesystem interaction.

**Run:**
```bash
python3 check-file.py
```

### ostasks.py
Automates Linux system administration tasks using Python:
- Creates users from a predefined list if they don't already exist
- Creates a user group if it doesn't exist
- Adds all users to the group
- Creates a shared directory with correct ownership and permissions

**Run (requires root):**
```bash
sudo python3 ostasks.py
```

### fabfile.py
Fabric automation script for local and remote task execution:
- `greeting(msg)` — prints a greeting
- `system_info()` — displays local disk, RAM, and uptime
- `remote_exec()` — runs commands on a remote server via SSH
- `web_setup(WEBURL, DIRNAME)` — deploys a website to a remote Apache server

**Run:**
```bash
fab greeting:msg=Morning
fab system_info
fab remote_exec -H targetserver
fab web_setup:WEBURL=<url>,DIRNAME=<dir> -H targetserver
```

## Key Concepts Covered
- `os` module — filesystem checks, system commands, directory creation
- `os.system()` — running shell commands from Python
- Python Fabric — local and remote task automation over SSH
- Exception handling
- Functions, modules, loops, conditions