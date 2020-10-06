    pipeline {
    agent any
    parameters{
            string(defaultValue: 'Israel', description: '', name: 'country1', trim: false)	            
            string(defaultValue: 'Russia', description: '', name: 'country2', trim: false)
            string(defaultValue: 'USA', description: '', name: 'country3', trim: false)
            string(defaultValue: 'Brazil', description: '', name: 'country4', trim: false)
            string(defaultValue: 'South+Korea', description: '', name: 'country5', trim: false)



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
            stage('inputs from user'){
            steps{
               script {
                    if(params){
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
    }
