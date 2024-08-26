pipeline {
    agent {
        docker {
            image 'jenkins-agent-python'
            label 'python-agent'
        }
    }

    environment {
        CONFIG_FILE = 'config.ini'
    }

    stages {
        stage('Load and Parse Config') {
            steps {
                script {
                    // Read the INI file content
                    def configText = readFile(CONFIG_FILE)
                    
                    // Parse the INI file
                    def config = parseIniFile(configText)

                    // Print the configuration for debugging
                    echo "Configuration: ${config}"

                    // Define project settings
                    def sectionName = 'default' // Example section name
                    def projectConfig = config[sectionName]

                    if (!projectConfig) {
                        error "Configuration for section '${sectionName}' not found in '${CONFIG_FILE}'."
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
                script {
                    if (env.REPO_URL && env.BRANCH_NAME) {
                        git branch: "${env.BRANCH_NAME}", url: "${env.REPO_URL}"
                    } else {
                        error "Repository URL or branch name not set."
                    }
                }
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

// Function to parse INI file content
def parseIniFile(String iniText) {
    def config = [:]
    def section = null

    iniText.split('\n').each { line ->
        line = line.trim()

        if (line.startsWith("[") && line.endsWith("]")) {
            section = line[1..-2]
            config[section] = [:]
        } else if (line && section && line.contains('=')) {
            def (key, value) = line.split('=', 2).collect { it.trim() }
            config[section][key] = value
        }
    }

    return config
}
