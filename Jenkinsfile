pipeline {
    agent any 

    stages {
        stage('Hola Mundo') {
            steps {
                script {
                    echo '¡Hola Fredy!'
                }
            }
        }
    }
}

agent {
        node 'nombre agente'
    }

Stage simple

        stage('nombre stage') {
            steps {
                script {
                    echo 'mensaje'
                    sh 'pip3 install -r requirements.txt -t '
                }
            }
        }
Stage con docker

        stage('nombre stage') {
            steps {
		        script {
                    docker.image('imagendocker').inside {
                        echo 'mensaje'
                        sh 'pip install coverage'
                    }
                }

            }
        }
