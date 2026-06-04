# Terraform AWS EC2 Deployment

## Overview
Infrastructure as Code project using Terraform to provision and configure
an AWS EC2 instance with Apache web server, security groups, key pairs,
and remote state storage in S3.

## Infrastructure Provisioned
| Resource | Description |
|---|---|
| aws_instance | t3.micro Ubuntu 22.04 EC2 instance |
| aws_security_group | Security group (dove-sg) |
| aws_vpc_security_group_ingress_rule | SSH (restricted IP) + HTTP (open) |
| aws_key_pair | SSH key pair for EC2 access |
| aws_ec2_instance_state | Ensures instance stays running |

## File Structure
| File | Purpose |
|---|---|
| provider.tf | AWS provider and region configuration |
| vars.tf | Input variables (region, AMI map, SSH user) |
| Instance.tf | EC2 instance resource with provisioners |
| SecGrp.tf | Security group and ingress/egress rules |
| Keypair.tf | SSH key pair resource |
| instID.tf | Data source for latest Ubuntu AMI + output |
| backend.tf | Remote state storage in AWS S3 |
| web.sh | Provisioning script — installs Apache |

## Provisioners Used
- **file** — uploads web.sh to the EC2 instance
- **remote-exec** — executes web.sh on the remote instance
- **local-exec** — saves private IP to private_ips.txt locally

## Remote State
Terraform state is stored remotely in AWS S3 for team collaboration
and state locking. Configure bucket name in terraform.tfvars.

## Usage
```bash
# Copy and configure variables
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values

# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy infrastructure
terraform destroy
```

## Key Concepts Demonstrated
- Provider configuration
- Resource blocks (EC2, Security Groups, Key Pairs)
- Input variables with defaults and maps
- Data sources (dynamic AMI lookup)
- Output values
- File, remote-exec, and local-exec provisioners
- Remote backend (S3)
- Variable maps for multi-region AMI selection