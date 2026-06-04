# Terraform — Infrastructure as Code

## What is Terraform?
Terraform is an open-source Infrastructure as Code (IaC) tool by HashiCorp.
It allows you to define, provision, and manage cloud infrastructure
using declarative configuration files (.tf files).

## Core Concepts

### Providers
Plugins that interact with cloud platforms (AWS, Azure, GCP).

    provider "aws" {
      region = var.region
    }

### Resources
The infrastructure components to create.

    resource "aws_instance" "web" {
      ami           = "ami-12345"
      instance_type = "t3.micro"
    }

### Variables
Input parameters to make configurations reusable.

    variable "region" {
      default = "us-east-1"
    }

### Outputs
Values exported after apply for use or reference.

    output "public_ip" {
      value = aws_instance.web.public_ip
    }

### Data Sources
Fetch existing resource information dynamically.

    data "aws_ami" "ubuntu" {
      most_recent = true
      owners      = ["099720109477"]
    }

### Backend
Where Terraform stores its state file.

    terraform {
      backend "s3" {
        bucket = "my-tf-state"
        key    = "terraform/backend"
        region = "us-east-1"
      }
    }

## Provisioners
Run scripts or commands during resource creation.

| Provisioner | Purpose |
|---|---|
| file | Upload files to remote resource |
| remote-exec | Run commands on remote resource via SSH |
| local-exec | Run commands on local machine |

## Terraform Workflow

    terraform init     # Download providers and initialize backend
    terraform plan     # Preview changes before applying
    terraform apply    # Create/update infrastructure
    terraform destroy  # Tear down all managed infrastructure

## State File
- Records what infrastructure Terraform manages
- Never commit terraform.tfstate to version control
- Use remote backend (S3) for team environments
- State locking prevents concurrent modifications

## Variable Maps (Multi-region AMI)

    variable "amiID" {
      type = map(string)
      default = {
        us-east-1 = "ami-abc123"
        us-east-2 = "ami-def456"
      }
    }
    # Usage
    ami = var.amiID[var.region]

## Security Best Practices
- Never hardcode AWS credentials in .tf files
- Never commit terraform.tfstate — use remote backend
- Never commit SSH keys or terraform.tfvars
- Restrict SSH ingress to your specific IP, not 0.0.0.0/0
- Use .gitignore to exclude sensitive files