pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {  
                 sh '''pwd'''
            }
        }
    }
}
}
