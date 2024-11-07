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
    }
}

