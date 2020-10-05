pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
         environment {
                  HOME="."
                }
            steps {
                sh 'python --version'
            }
        }
    }
}
