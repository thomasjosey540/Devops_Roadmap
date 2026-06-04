# Python for DevOps

## Why Python for DevOps?
Python is the primary scripting language for DevOps automation.
It is used for infrastructure automation, cloud interaction,
monitoring scripts, and tooling.

## Core Concepts Covered

### Variables & Data Types
- Strings, integers, lists, dictionaries
- Print formatting: `"Hello {}".format(name)`

### Conditions & Loops
- if/elif/else for branching logic
- for loops for iterating over lists
- break and continue for loop control

### Functions
- Defining reusable functions with `def`
- Passing arguments, returning values
- Docstrings for documentation

### Modules
- Importing built-in modules: `import os`
- Using module functions: `os.path.isfile()`, `os.system()`

### OS Module
- `os.path.isfile(path)` — check if file exists
- `os.path.isdir(path)` — check if directory exists
- `os.system(cmd)` — run shell commands from Python
- `os.mkdir(path)` — create directory
- Exit codes: 0 = success, non-zero = failure

### Exception Handling
```python
try:
    # code that might fail
except Exception as e:
    print("Error: {}".format(e))
finally:
    # always runs
```

## Python Fabric
Fabric is a Python library for automating local and remote
shell commands over SSH.

### Key Functions
- `local(cmd)` — run command on local machine
- `run(cmd)` — run command on remote server
- `sudo(cmd)` — run command with sudo on remote server
- `put(local, remote)` — upload file to remote server
- `lcd(path)` — change local directory
- `cd(path)` — change remote directory

### env object
- `env.user` — SSH username for remote connections

## Cloud Interaction — Boto3
Boto3 is the official AWS SDK for Python.
Allows Python scripts to interact with AWS services
programmatically — EC2, S3, RDS, and more.

```python
import boto3
ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_instances()
```

## AI for Cloud Automation
Using AI tools (Copilot, ChatGPT) to:
- Generate Boto3 scripts for AWS tasks
- Write automation scripts faster
- Debug Python errors