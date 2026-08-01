pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Repository hazır.'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t rahmann1992/my-service:latest .'
            }
        }

        stage('Test Image') {
            steps {
                sh 'docker images | grep my-service'
            }
        }
    }
}
