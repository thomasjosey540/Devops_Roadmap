terraform {
  backend "s3" {
    bucket = var.tf_state_bucket
    key    = "terraform/backend"
    region = "us-east-1"
  }
}