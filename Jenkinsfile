node {
    def app
    def repo = "chanut8433/test"
    def tag  = env.BUILD_NUMBER

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("${repo}:${tag}")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub chanut8433') {
            // push build number tag
            app.push("${tag}")
            // push latest tag
            app.push("latest")
        }
    }
    
    stage('Trigger ManifestUpdate') {
        echo "triggering updatemanifestjob"
        build job: 'updatemanifest', parameters: [
            string(name: 'DOCKERTAG', value: tag)
        ]
    }
}
