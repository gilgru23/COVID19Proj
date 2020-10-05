pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'nohup python app.py' 
                sh 'curl http://127.0.0.1:5000/newCasesPeak?country=israel'
            }
        }
    }
}
