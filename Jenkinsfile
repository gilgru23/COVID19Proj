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
                params.each { key, value ->
                sh "curl http://127.0.0.1:5000/newCasesPeak?country=${value}"
                sh "curl http://127.0.0.1:5000/recoveredPeak?country=${value}"
                sh "curl http://127.0.0.1:5000/deathsPeak?country=${value}"
                }
            }
            }
        }
    }
    }
