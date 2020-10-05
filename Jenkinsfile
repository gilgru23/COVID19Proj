pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh """
. .env/bin/activate
pip install -r requirements.txt
"""
            }
        }
    }
}
