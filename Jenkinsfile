pipeline {
    agent any

    stages {
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/CESAG-IT/sen-immo-app.git", branch: "main"
            }
        }

        stage("Build") {
            steps {
                echo "Building the Docker image"
                sh "docker build -t sen-immo-app ."
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "Pushing the Docker image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "dockerHub", passwordVariable: "dckr_pat_8_7p8veI6pfrAmc9xLiiOFn9-BI", usernameVariable: "lionnelpat")]) {
                    sh "docker tag sen-immo-app ${env.dockerHubUser}/sen-immo-app:latest"
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker push ${env.dockerHubUser}/sen-immo-app:latest"
                }
            }
        }

        stage("Deploy") {
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}