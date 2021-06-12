pipeline {
    agent {
        label '!docker-helm'
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t hassnainalvi021/flask-app .'
                sh 'docker push hassnainalvi021/flask-app .'
            }
        }
        stage('deploy') {
            steps {
                sh 'helm upgrade --install flask-app chart/ '
            }
        }
    }
}