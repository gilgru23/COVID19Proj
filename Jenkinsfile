    pipeline {
    agent any
        properties{
            ([parameters([string(defaultValue: 'Israel', description: '', name: 'country', trim: false)])])
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
                sh 'curl http://127.0.0.1:5000/newCasesPeak?country=${params[0]}'
                sh 'curl http://127.0.0.1:5000/recoveredPeak?country=USA'
                sh 'curl http://127.0.0.1:5000/deathsPeak?country=Japan'
            }
            }
        }
    }

