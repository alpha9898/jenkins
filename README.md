# Jenkins CI Demo Project

This project demonstrates a basic Jenkins CI pipeline for a Dockerized Flask application.

## Project Structure

```
jenkins-demo/
├── app.py           # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker image configuration
├── Jenkinsfile      # Jenkins pipeline definition
└── README.md        # This file
```

## Pipeline Stages

1. **Clone Repository** - Pull source code from GitHub
2. **Build Docker Image** - Build the Docker image with build number tag
3. **Run Container** - Stop any existing container and run the new one

## Technologies

- **Jenkins** - CI/CD automation server
- **Docker** - Containerization platform
- **GitHub** - Source code repository
- **Python (Flask)** - Web application framework

## Local Testing

Before pushing to Jenkins, you can test locally:

```bash
# Build the Docker image
docker build -t jenkins-demo .

# Run the container
docker run -p 5000:5000 jenkins-demo

# Access the app at http://localhost:5000
```

## Jenkins Setup

### Prerequisites

1. Jenkins installed and running
2. Docker installed on Jenkins server
3. Jenkins user added to docker group:
   ```bash
   sudo usermod -aG docker jenkins
   sudo systemctl restart jenkins
   ```

### Creating the Pipeline Job

1. Open Jenkins → **New Item**
2. Enter name: `jenkins-demo`
3. Select **Pipeline** → OK
4. In Pipeline section:
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/<your-username>/jenkins-demo.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`
5. **Save** → **Build Now**

## Result

After a successful build:
- Docker image is created with tag `jenkins-demo:<build-number>`
- Container runs on port 5000
- Application accessible at `http://<server-ip>:5000`

### Pipeline Execution Screenshot

![Jenkins Pipeline Success](image.png)

*The screenshot above shows a successful Jenkins pipeline execution (Build #3) with all stages completed:*

| Stage | Duration | Status |
|-------|----------|--------|
| Checkout SCM | 1.1s | ✅ Success |
| Clone Repository | 1.0s | ✅ Success |
| Build Docker Image | 4.0s | ✅ Success |
| Run Container | 2.8s | ✅ Success |
| Post Actions | 61ms | ✅ Success |

**Total Build Time:** 11 seconds

The pipeline successfully deployed the Flask application, now running at `http://localhost:5000`

## Future Enhancements

- [ ] Add GitHub Webhooks for automatic builds
- [ ] Add automated tests stage
- [ ] Push images to Docker Hub
- [ ] Deploy to Kubernetes

## Author

Junior DevOps Engineer - Jenkins CI/CD Demo Project

