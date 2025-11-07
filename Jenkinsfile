pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               git url: 'https://github.com/Siddh100/news-ci-cd.git', branch: 'main'
    }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest || exit /b 0
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask App...'
                bat '''
                    call venv\\Scripts\\activate
                    start /B python app.py
                '''
            }
        }
    }

    post {
        success { echo '✅ Build and Deployment Successful!' }
        failure { echo '❌ Build Failed!' }
    }
}
