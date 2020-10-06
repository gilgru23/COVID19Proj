    pipeline {
    agent any
        parameters{
            string(defaultValue: 'Israel', description: '', name: 'country', trim: false)
        }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                 withEnv(['JENKINS_NODE_COOKIE=dontkill']) {
                    sh 'nohup python app.py &'
                } 
            }
            }
            stage('tests'){
            steps{
               script {
                  params.each() {
                     echo it
                  }
            }
            }
        }
    }
    }
