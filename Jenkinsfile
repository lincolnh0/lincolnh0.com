pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "docker context use default"
                sh "docker-compose -f test.yml build"
                sh "docker-compose -f test.yml up -d"
                sh "docker-compose -f test.yml run --rm django python manage.py migrate"
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        echo 'Running tests...'
                        sh "docker-compose -f test.yml run --rm django pytest"
                    }
                    catch (exc) {
                        echo 'Testing failed!'
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -r lincolnh0:~/.production .envs/"
                sh "docker context use lincolnh0"
                sh "docker-compose -f production.yml build"
                sh "docker-compose -f production.yml up --no-deps -d django"
                sh "docker-compose -f production.yml run --rm django python manage.py makemigrations"
                sh "docker-compose -f production.yml run --rm django python manage.py migrate"
            }
        }
        stage('Tidy up') {
            steps {
                sh "docker context use default"
                sh "docker-compose -f test.yml stop"
            }
        }
    }
}
