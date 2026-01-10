pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKERHUB_REPO = 'amaryasser046/jenkins-demo'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pytest test_app.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKERHUB_REPO%:%BUILD_NUMBER% -t %DOCKERHUB_REPO%:latest ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin"
                bat "docker push %DOCKERHUB_REPO%:%BUILD_NUMBER%"
                bat "docker push %DOCKERHUB_REPO%:latest"
                bat "docker logout"
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker stop jenkins-demo || exit 0'
                bat 'docker rm jenkins-demo || exit 0'
                bat "docker run -d -p 5000:5000 --name jenkins-demo %DOCKERHUB_REPO%:%BUILD_NUMBER%"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! App running at http://localhost:5000'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
