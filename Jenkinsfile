
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                    sh """
    . .env/bin/activate
    pip install -r requirements/test.txt
    """
                 sh 'python app.py' 
            }
        }
    }
}
