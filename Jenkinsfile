
pipeline {
    agent any
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
