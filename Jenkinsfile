pipeline {
    agent any

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
                bat 'docker build -t jenkins-demo:%BUILD_NUMBER% .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker stop jenkins-demo || exit 0'
                bat 'docker rm jenkins-demo || exit 0'
                bat 'docker run -d -p 5000:5000 --name jenkins-demo jenkins-demo:%BUILD_NUMBER%'
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
