# HeroVired_Capstone-project_Batch-16B


# End-to-End DevOps Pipeline for a Web Application with CI/CD

## Sprint 1: Application and Development Environment

### Objective
Prepare the development environment, create a sample web application,
write automated tests, and package the application using Docker.

### Tools
- Visual Studio Code
- Python and Flask
- Pytest
- Docker Desktop
- Windows PowerShell

### Application Endpoints
- `/` — Returns application information.
- `/health` — Returns the application health status.

### Implementation
The application is implemented using Flask. Automated tests validate
the home endpoint and health endpoint. A Dockerfile packages the
application into a container image.

### Validation
- [ ] Python environment configured
- [ ] Dependencies installed
- [ ] Automated tests passed
- [ ] Application runs locally
- [ ] Docker image built successfully
- [ ] Container starts successfully
- [ ] Home endpoint returns HTTP 200
- [ ] Health endpoint returns HTTP 200

### Evidence
Screenshots are stored in the `screenshots` directory.



# Sprint 1 — Test Cases

| Test ID | Test Description | Expected Result | Status |
|---|---|---|---|
| TC-01 | Run automated home endpoint test | Test passes | Success |
| TC-02 | Run automated health endpoint test | Test passes | Success |
| TC-03 | Request the home endpoint locally | HTTP 200 and application message | Success |
| TC-04 | Request the health endpoint locally | HTTP 200 and healthy status | Success |
| TC-05 | Build the Docker image | Build succeeds | Success |
| TC-06 | Start the Docker container | Container is running | Success |
| TC-07 | Request the home endpoint in Docker | HTTP 200 and application message | Success |
| TC-08 | Request the health endpoint in Docker | HTTP 200 and healthy status | Success |

Update each status to `Pass` only after you have verified the corresponding test.



### Sprint Outcome
Complete this section after all validation steps succeed.
Record any issues and their resolutions before closing Sprint 1.

### Sprint 1 checklist 

Project folders match the agreed architecture
- [ ] Flask application runs locally
- [ ] Both automated tests pass
- [ ] Home endpoint returns the expected response
- [ ] Health endpoint returns healthy status
- [ ] Docker image builds successfully
- [ ] Docker container starts successfully
- [ ] Both endpoints work through Docker
- [ ] Screenshots are saved in the screenshots folder
- [ ] Sprint report and test-case documents are saved
- [ ] Git commit is created

## Sprint 2 — AWS infrastructure with Terraform

Prepare the Terraform configuration for networking, IAM, ECR and EKS, along with the required state-management setup. We will validate the AWS region, permissions and expected costs before provisioning resources.

The goal for this sprint is to prepare and validate the Terraform configuration for AWS networking, IAM, Amazon ECR, Amazon EKS, and remote Terraform state. We'll validate permissions and estimated costs before creating paid AWS resources.

### Tools

- [ ] AWS Management Console

- [ ] AWS CLI

- [ ] Terraform

- [ ] Visual Studio Code

- [ ] Windows PowerShell

- [ ] Amazon VPC

- [ ] Amazon EC2

- [ ] Amazon ECR

- [ ] Amazon EKS

- [ ] Amazon S3

- [ ] AWS IAM

- [ ] Jenkins

###  AWS Configuration

- [ ] AWS Region: ap-south-1 (Mumbai)

- [ ] ECR Repository: devops-capstone-app

- [ ] EKS Cluster: devops-capstone-dev

- [ ] Terraform State Storage: Amazon S3

- [ ] Infrastructure Provisioning: Terraform

### Implementation

Terraform configuration files are organized to manage AWS infrastructure.

The configuration covers:

- [ ] AWS provider and region configuration.

- [ ] VPC and subnet creation.

- [ ] Internet Gateway and routing configuration.

- [ ] Security groups and network access.

- [ ] IAM roles and policies for EKS.

- [ ] Amazon ECR repository creation.

- [ ] Amazon EKS cluster and worker node configuration.

- [ ] S3 backend configuration for Terraform state management.

Terraform commands are used to format, initialize, validate, plan, and apply infrastructure configurations.

The Terraform configuration is also prepared for execution through Jenkins to support automated infrastructure provisioning.

### Recommended evidence:

- [ ] Terraform project structure.

- [ ] Terraform initialization and validation.

- [ ] Terraform plan output.

- [ ] S3 bucket and versioning configuration.

- [ ] AWS VPC and subnet details.

- [ ] ECR repository details.

- [ ] EKS cluster status.

- [ ] EKS node group status.

- [ ] Jenkins Terraform execution.

## Sprint Outcome

Terraform configurations were prepared to provision and manage AWS networking, IAM, ECR, and EKS resources.

The remote state-management configuration was prepared using Amazon S3 to support consistent infrastructure management.

Record any provisioning issues, IAM permission errors, state-management problems.

## Sprint 3: Configuration Management with Ansible and Jenkins

### Objective

Automate server configuration and software installation using Ansible. Prepare Ansible playbooks to configure EC2 instances and install the required DevOps tools and dependencies.

Integrate Ansible with Jenkins to automate configuration management after infrastructure provisioning.

### Configuration Scope

EC2 instance configuration.

Operating system package management.

Git installation and verification.

Docker installation and configuration where required.

AWS CLI installation and verification.

kubectl installation and verification.

Required deployment dependencies.

Server connectivity and access validation.
