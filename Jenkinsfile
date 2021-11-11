pipeline {
    parameters {
        booleanParam(name: 'BASIC_TESTS', defaultValue: true, description: 'Run basic tests?')
        booleanParam(name: 'PYTEST', defaultValue: true, description: 'Run  pytest?')
        booleanParam(name: 'MIGRATE', defaultValue: false, description: 'Run migrations?')
    }
    agent any

    stages {
        stage('Basic Tests') {
            when {
                expression { params.BASIC_TESTS == true }
            }
            steps {
                fileExists("local.yml")
                fileExists("test.yml")
                fileExists("production.yml")
                fileExists("manage.py")
                fileExists("config/settings/base.py")
                fileExists("config/settings/local.py")
                fileExists("config/settings/production.py")
            }
        }
        stage('Build') {
            when {
                expression { params.PYTEST == true }
            }
            steps {
                sh "docker-compose -f test.yml build"
                sh "docker-compose -f test.yml up -d"
                sh "docker-compose -f test.yml run --rm django python manage.py migrate"
            }
        }
        stage('Test') {
            when {
                expression { params.PYTEST == true }
            }
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
                sh "docker-compose --context lincolnh0 -f production.yml build"
                sh "docker-compose --context lincolnh0 -f production.yml up --no-deps -d django"
                sh "docker-compose --context lincolnh0 -f production.yml run --rm django python manage.py migrate"
            }
        }
        stage('Tidy up') {
            steps {
                sh "docker-compose -f test.yml stop"
            }
        }
    }
}
