pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-demo:${BUILD_NUMBER} .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop jenkins-demo || true
                docker rm jenkins-demo || true
                docker run -d -p 5000:5000 --name jenkins-demo jenkins-demo:${BUILD_NUMBER}
                '''
            }
        }
    }
}

