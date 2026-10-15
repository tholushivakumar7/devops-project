
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smartnest-ai'
        CONTAINER_NAME = 'smartnest-ai-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/tholushivakumar7/devops-project.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest -v test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        --restart unless-stopped \
                        -p 8000:8000 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    for i in $(seq 1 10); do
                        if curl -fsS http://localhost:8000/health; then
                            echo "Health check passed"
                            exit 0
                        fi
                        sleep 3
                    done
                    echo "Health check failed"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'SmartNest AI deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
