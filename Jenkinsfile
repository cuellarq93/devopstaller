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
                    echo 'Ejecutando pruebas...'
                    sh '''pip install coverage
                          coverage run -m unittest discover -s tests
                          coverage xml -o coverage.xml'''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    docker.image('sonarsource/sonar-scanner-cli:latest').inside {
                        withSonarQubeEnv('SonarCloud') {
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

        stage('Deploy') {
            steps {
                script {
                    docker.image('darkaru/sam:1.33-amd').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws']]) {
                            echo 'Desplegando la aplicación...'
                            sh 'sam deploy -t template.yml --stack-name nombreusuario --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --resolve-s3'
                        }
                    }
                }
            }
        }
    }
}
