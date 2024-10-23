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

                        echo 'install coverage'
                        sh 'pip install coverage'
                    }
                }
            }
        }
        stage('test') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        echo 'run coverage'
                        sh 'coverage run -m unittest discover -s tests'
                        echo 'coverage to xml'
                        sh 'coverage xml -o coverage.xml'
                    }

                }
            }
        }
        stage('sonar') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside {
                        withSonarQubeEnv('ingfrecab') {
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