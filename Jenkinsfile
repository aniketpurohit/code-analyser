pipeline {
    agent any

    parameters {
        choice(name: 'PROJECT', choices: ['default', 'project1', 'project2', 'staging', 'production'], description: 'Select the project configuration.')
    }

    environment {
        CONFIG_FILE = 'config.ini'
    }

    stages {
        stage('Load Configuration') {
            steps {
                script {
                    def config = readIniFile file: "${CONFIG_FILE}"
                    def projectConfig = config[params.PROJECT]
                    
                    if (projectConfig == null) {
                        error "Configuration for project '${params.PROJECT}' not found in '${CONFIG_FILE}'."
                    }

                    env.REPO_URL = projectConfig['repo_url']
                    env.BRANCH_NAME = projectConfig['branch_name']
                    env.PYTHON_FILES = projectConfig['python_files']
                    env.TEST_COMMAND = projectConfig['test_command']
                    env.REQUIREMENTS_FILE = projectConfig['requirements_file']
                }
            }
        }

        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}", url: "${env.REPO_URL}"
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r ${env.REQUIREMENTS_FILE}
                '''
            }
        }

        stage('Static Code Analysis') {
            steps {
                script {
                    sh "pylint ${env.PYTHON_FILES}"
                    sh "flake8 ."
                    sh "black --check ."
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    ${env.TEST_COMMAND}
                    '''
                }
            }
        }

        stage('Archive Results') {
            steps {
                junit '**/test-*.xml'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
