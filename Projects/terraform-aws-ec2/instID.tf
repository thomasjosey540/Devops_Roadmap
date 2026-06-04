# Data source to fetch the latest Ubuntu 22.04 AMI dynamically
data "aws_ami" "amiID" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  # Canonical's AWS account ID
  owners = ["099720109477"]
}

output "instance_id" {
  description = "The ID of the latest Ubuntu 22.04 AMI"
  value       = data.aws_ami.amiID.id
}