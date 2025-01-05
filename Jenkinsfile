pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pull code from version control (e.g., GitHub)
                git url: 'https://github.com/your-repo/weather-web.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                // Run build commands (adjust based on your project)
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                // Run tests
                sh 'npm test'
            }
        }
        stage('Docker Build and Deploy') {
            steps {
                // Build Docker image
                sh 'docker build -t weatherelza:latest .'
                // Run Docker container
                sh 'docker run -d -p 5000:5000 weatherelza:latest'
            }
        }
    }
    post {
        always {
            // Notify and cleanup
            echo 'Pipeline completed'
        }
    }
}
