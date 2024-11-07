pipeline {
    agent {
        node 'prueba-ivan'
    }

    stages {
        

           stage('docker-ivan') {

            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'envopassausar']]) {
                            echo 'mensaje'
                            sh 'comando'
                        }
                    }
                }
            }
        }    
    }
}

