pipeline {
    agent {
        node 'agent'
    }

    stages {
        stage('Hola Mundo StMurilloR') {
            steps {
                script {
                    echo '¡Hola Mundo StMurilloR!'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.image('python:3.9.20-alpine').inside('-v /tmp:/tmp') {
                        echo 'Installing dependencies..'
                        sh 'pip3 install -r requirements.txt -t /tmp'
                    }
                }
            }
        }

        stage('test') {
                steps {
    		        script {                        
                            echo 'Running tests and reporting..'
                            sh '''
                            pip install coverage --prefix /tmp
                            coverage run -m unittest discover -s tests
                            coverage xml -o /tmp/coverage.xml
                        '''
                    }
                }
            }
        

        stage('sonar') {
            steps {
                script {
                    docker.image('sonarsource/sonar-scanner-cli:latest').inside('-v /tmp:/tmp') {
                        withSonarQubeEnv('SonarCloud') {
                            sh '''
                            sonar-scanner \
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
                            echo 'Deploying App with AWS..'
                            sh '''
                                sam deploy -t template.yml \
                                --stack-name branch-StMurilloR \
                                --region us-east-1 \
                                --capabilities CAPABILITY_NAMED_IAM \
                                --resolve-s3
                            '''
                        }
                    }
                }
            }
        }

        //Condicional ramas va despues del stage y antes del step

            when {
                anyOf {
                    branch 'branch-StMurilloR'
                }
            }
    }
}
