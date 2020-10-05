pipeline {
    agent any
        stage('build') {
            steps {
                 sh 'pip install requirements.txt'
                 sh 'python app.py' 
        }
    }
}
