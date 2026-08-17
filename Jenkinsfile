pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile hello.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests'
            }
        }

        stage('Verify') {
            steps {
                bat 'echo "CI verification completed"'
            }
        }
    }
}
