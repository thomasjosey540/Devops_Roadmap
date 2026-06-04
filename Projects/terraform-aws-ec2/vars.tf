variable "region" {
  default = "us-east-1"
}

variable "zone1" {
  default = "us-east-1a"
}

variable "webuser" {
  default = "ubuntu"
}

variable "amiID" {
  type = map(string)
  default = {
    us-east-1 = "ami-091138d0f0d41ff90"
    us-east-2 = "ami-0fe18bc3cfa53a248"
    us-west-1 = "ami-06c77cb49ac92a541"
  }
}

variable "my_ip" {
  description = "Your public IP address for SSH access"
  default     = "0.0.0.0/0"  # Override with your actual IP
}

variable "public_key" {
  description = "SSH public key for EC2 key pair"
  default     = ""  # Set via terraform.tfvars or environment variable
}

variable "tf_state_bucket" {
  description = "S3 bucket name for Terraform remote state"
  default     = ""  # Set via terraform.tfvars
}