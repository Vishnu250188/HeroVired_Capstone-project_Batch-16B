variable "aws_region" {
  description = "AWS region for the capstone"
  type        = string
  default     = "ap-south-1"
}

variable "cluster_version" {
  description = "EKS Kubernetes version supported in the selected region"
  type        = string
}

variable "admin_cidr" {
  description = "Your public IP address in CIDR format, for example 203.0.113.10/32"
  type        = string

  validation {
    condition     = can(cidrnetmask(var.admin_cidr))
    error_message = "Provide a valid IPv4 CIDR, ideally your public IP with /32."
  }
}

variable "node_instance_types" {
  description = "EC2 instance types for EKS managed nodes"
  type        = list(string)
  default     = ["t3.medium"]
}
