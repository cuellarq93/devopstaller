pipeline {
    agent {
        node 'agent'
    }

    stages {
          stage('build') {
            steps {
                script {
                    echo 'Build'
		     docker.image('python:3.9.20-alpine').inside {
                          sh 'pip3 install -r requirements.txt -t .'
                    }
                
                }
            }
        }
        stage('Test') {
            steps {
		script {                   
			echo 'Test'
			sh 'pip install coverage'
			sh 'coverage run -m unittest discover -s tests'
			sh 'coverage xml -o coverage.xml'                    
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
           stage('Deploy') {
            steps {
                script {
                    docker.image('darkaru/sam:1.33-amd').inside {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws']]) {
                            echo 'Deploy'
                            sh 'sam deploy -t template.yml --stack-name menesesd --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --resolve-s3'
                            def outputValue = sh(script: """
                                    aws cloudformation describe-stacks \
                                    --stack-name menesesd \
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
        stage('Clear WS') {
            steps {
                script {
                    cleanWs()
                }
            }
        }
        stage('Clone repository') {
            steps {
                script {
                    git credentialsId: 'cuellarq', branch: 'main', url: 'https://github.com/cuellarq93/api-auto.git'
                }
            }
        }
        stage('Build image') {
            steps {
                script {
                    def imageName = 'menesesd'
                    docker.build(imageName)
                    docker.image(imageName).inside {
                          sh 'mvn serenity:aggregate'
                    }
                }
            }
        }
     
        stage('Publih') {
            steps {
                script {
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
}
