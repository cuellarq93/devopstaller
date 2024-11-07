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
                    echo 'Instalando dependencias...'
                    sh 'pip3 install -r requirements.txt -t .'
                }
            }
        }	
}
