pipeline {
    agent any

    environment {
        CONFIG_FILE = 'config.ini'
    }

    stages {
        stage('Process Projects') {
            steps {
                script {
                    // Read the configuration file
                    def config = readIniFile file: "${CONFIG_FILE}"

                    // Loop through each section in the configuration
                    config.each { sectionName, sectionConfig ->
                        if (sectionName != "default") {
                            echo "Processing project: ${sectionName}"

                            // Extract environment variables dynamically for each project
                            def repoUrl = sectionConfig['repo_url']
                            def branchName = sectionConfig['branch_name']
                            def pythonFiles = sectionConfig['python_files']
                            def testCommand = sectionConfig['test_command']
                            def requirementsFile = sectionConfig['requirements_file']

                            // Execute the pipeline stages for this project
                            stage("Checkout ${sectionName}") {
                                steps {
                                    git branch: "${branchName}", url: "${repoUrl}"
                                }
                            }

                            stage("Set Up Environment for ${sectionName}") {
                                steps {
                                    sh '''
                                    python -m venv venv
                                    source venv/bin/activate
                                    pip install -r ${requirementsFile}
                                    '''
                                }
                            }

                            stage("Static Code Analysis for ${sectionName}") {
                                steps {
                                    sh "flake8 ${pythonFiles}"
                                    sh "black --check ${pythonFiles}"
                                }
                            }

                            stage("Run Unit Tests for ${sectionName}") {
                                steps {
                                    sh '''
                                    source venv/bin/activate
                                    ${testCommand}
                                    '''
                                }
                            }

                            stage("Archive Results for ${sectionName}") {
                                steps {
                                    junit '**/test-*.xml'
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
