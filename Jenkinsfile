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
        stage('Build') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Instalando dependencias...'
                        sh 'pip3 install -r requirements.txt -t .'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Ejecutando pruebas...'
                        sh '''pip install coverage
                               coverage run -m unittest discover -s tests
                               coverage xml -o coverage.xml'''
                    }
                }
            }
        }
    }
}
