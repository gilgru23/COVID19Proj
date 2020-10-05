pipeline {
    agent any
    stages ('preInstallations') {
        sh 'pip install requirements.txt'
    }
        stage('build') {
            steps {
                 sh 'python app.py' 
        }
    }
}
}
