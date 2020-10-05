pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                                sh 'virtualenv venv --distribute'
                sh 'source venv/bin/activate '
                sh 'pip install --user -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}

