pipeline {
    agent {
        node 'agent'
    }

    stages {
        

           stage('Script Docker') {

            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                       sh '''
                            pip install -r requirements.txt -t .
                        '''
                    }
                }
            }
        }  

        stage('Test') {
            steps {
                script {
                        sh '''
                            pip install coverage
                            coverage run -m unittest discover -s tests
                            coverage xml -o coverage.xml
                        '''
                    
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
    }
}

