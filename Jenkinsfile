pipeline {
    agent any 

    stages {
        stage('Hola Mundo') {
            steps {
                script {
                    echo '¡Hola Mundo!'
                }
            }
        }
    }
    
   stage('build') {
            steps {
		script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Instalando dependencias...'
                        sh 'pip3 install -r requirements.txt -t .'
                }
            }
        }
    }
}
