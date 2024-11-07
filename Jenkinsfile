pipeline {
    agent {
        node 'ivanmolina20225'
    }

    stages {
        stage('script') {
            steps {
                script {
                    echo 'mensaje'
                    sh 'comando' 
                }
            }
        }

        stage('imagendocker') {
            steps {
                script {
                    docker.image('imagendocker').inside {
                        echo 'mensaje'
                        sh 'comando'
                    }
                }
            }
        }       
    }
}

