pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '/usr/local/bin/pip install --user -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}
