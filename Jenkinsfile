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

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push rahmann1992/my-service:latest'
            }
        }
    }
}
