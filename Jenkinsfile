pipeline {
    agent {
        node 'agent'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Instalando dependencias...'
                        sh '''
                            python -m venv venv
                            . ./venv/bin/activate
                            pip install --no-cache-dir --upgrade -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Ejecutando pruebas...'
                        sh '''
                            python -m venv venv
                            . ./venv/bin/activate
                            pip install --no-cache-dir --upgrade coverage
                            coverage run -m unittest discover -s tests
                            coverage xml -o coverage.xml
                        '''
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    docker.image('sonarsource/sonar-scanner-cli:latest').inside {
                        withSonarQubeEnv('SonarCloud') {
                            echo 'Ejecutando análisis de SonarQube...'
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
                            echo 'Desplegando aplicación...'
                            sh '''sam deploy -t template.yml --stack-name mockapi --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --resolve-s3'''
                            def outputValue = sh(script: """
                                aws cloudformation describe-stacks \
                                --stack-name mockapi \
                                --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' \
                                --output text \
                                --region us-east-1""",
                            returnStdout: true)
                            echo "Output value is: ${outputValue}"
                            env.OUTPUT_VALUE = outputValue
                        }
                    }
                }
            }
        }
        stage('Clean Workspace') {
            steps {
                // Limpia el workspace actual
                cleanWs()
            }
        }
        stage('Clone Repository') {
            steps {
                // Clona el repositorio usando las credenciales
                git credentialsId: 'cuellarq', branch: 'main', url: 'https://github.com/cuellarq93/api-auto.git'
            }
        }
        stage('Use CloudFormation Output') {
            steps {
                script {
                    sh "ls -la"
                    echo "Using CloudFormation Output: ${env.OUTPUT_VALUE}" // outputValue no estará disponible aquí
                }
            }
        }
        stage('Build and Test with Docker') {
            steps {
                script {
                    // Construir la imagen de Docker
                    def imageName = 'serenity-cucumber-test'
                    docker.build(imageName)

                    // Ejecutar el contenedor que ejecuta las pruebas
                    docker.image(imageName).inside {
                        sh "ls -la"
                        sh "mvn serenity:aggregate "
                        //sh "mvn clean verify -Dapi.url=${env.OUTPUT_VALUE}"
                    }
                }
            }
        }
        stage('Publish Report') {
            steps {
                // Publica el reporte de Serenity en el pipeline
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'target/site/serenity',
                    reportFiles: 'index.html',
                    reportName: 'Serenity Test Report'
                ])
            }
        }
    }
}
