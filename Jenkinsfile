pipeline {
    agent {
        node 'agent'
    }

    stages {
        stage('build') {
            steps {
		        script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'install requirements'
                        sh 'pip3 install -r requirements.txt -t .'
                    }
                }
            }
        }
        stage('test') {
            steps {
                script {
                   echo 'install coverage'
                   sh 'pip install coverage'
                   echo 'run coverage'
                   sh 'coverage run -m unittest discover -s tests'
                   echo 'coverage to xml'
                   sh 'coverage xml -o coverage.xml'

                }
            }
        }
        stage('sonar') {
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

        stage('deploy aws') {

            steps {
                script {
                    docker.image('darkaru/sam:1.33-amd').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws']]) {
                            echo 'deploy sam'
                            sh 'sam deploy -t template.yml --stack-name ingfrecab --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --resolve-s3'
                        }
                    }
                }
            }
        }
    }
}