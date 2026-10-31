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
