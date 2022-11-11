variable "bucket_name" {
  type        = string
  description = "S3 Bucket name"
  default     = "lastattpemtbeforesunrise"
}
variable "aws_region" {
  default = "eu-central-1"
}

variable "aws_profile" {
  default = "DanielDimitrov1"
}

variable "aws_account" {
  type    = string
  default = "443390603815"
}

variable "env" {
  type    = string
  default = "project"
}

variable "app" {
  type    = string
  default = "final"
}

variable "name_container" {
  default = "container"
}

variable "web_server_image" {
  default     = "443390603815.dkr.ecr.eu-central-1.amazonaws.com/daniel"
}

variable "image_tag" {
  type    = string
  default = "0.0.1"
}

variable "github_oauth_token" {
  type    = string
  default = ""
}

variable "repo_url" {
  type    = string
  default = "https://github.com/DanielDimitrov1/final.git"
}

variable "branch_pattern" {
  type    = string
  default = "main"
}
variable "git_trigger_event" {
  type    = string
  default = "PUSH"
}
variable "app_count" {
  default = 1
}
