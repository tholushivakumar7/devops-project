
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smartnest-ai'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace.'
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
    }

    post {
        success {
            echo 'SmartNest AI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
