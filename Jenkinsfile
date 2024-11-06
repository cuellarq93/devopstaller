pipeline {
    agent {
        node 'agent'
    }

    stages {
          stage('build') {
            steps {
                script {
                    echo 'Build'
                    sh 'pip3 install -r requirements.txt -t .'
                }
            }
        }
        stage('Test') {
            steps {
		        script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'Test'
                        sh 'pip install coverage'
                        sh 'coverage run -m unittest discover -s tests'
                        sh 'coverage xml -o coverage.xml'
                    }
                }

            }
        }
        stage('Sonar') {
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
        stage('Deply') {
            steps {
                script {
                    docker.image('darkaru/sam:1.33-amd').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'envopassausar']]) {
                            echo 'Deply'
                            sh 'sam deploy -t template.yml --stack-name aws --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --resolve-s3'
                        }
                    }
                }
            }
        }

    }
}
