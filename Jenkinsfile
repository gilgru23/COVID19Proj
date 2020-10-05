pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}
