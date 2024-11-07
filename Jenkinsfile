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

        stage('devopsBullgrof') {
            steps {
                script {
                    echo 'mensaje'
                    sh 'pip3 install -r requirements.txt -t '
                }
            }
        }
Stage con docker

        stage('devopsBullgrof') {
            steps {
		        script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'mensaje'
                        sh 'pip install coverage'
                    }
                }

            }
        }

stage('devopsBullgrof') {
            steps {
                script {
                    docker.image('sonarsource/sonar-scanner-cli:latest').inside {
                        withSonarQubeEnv('envopassausar') {
                            sh '''sonar-scanner \
                                -Dsonar.projectKey=cuellarq_devopsclass \
                                -Dsonar.organization=cuellarq \
                                -Dsonar.host.url=https://sonarcloud.io \
                                -Dsonar.login=$SONAR_TOKEN \
                                -Dsonar.sources=src/ \
                                -Dsonar.language=py \
                                -Dsonar.sources=src \
                                -Dsonar.tests=tests \
                                -Dsonar.test.inclusions=**/*_test.py \
                                -Dsonar.python.coverage.reportPaths=coverage.xml'''
                        }
                    }
                }
            }
        } 

 stage('devopsBullgrof') {

            steps {
                script {
                    docker.image('darkaru/sam:1.33-amd').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws']]) {
                            echo 'mensaje'
                            sh 'comando'
                        }
                    }
                }
            }
        }


  when {
                anyOf {
                    branch 'nombrerama'
                    branch 'nombrerama'
                    branch 'nombrerama'
                }
            }
