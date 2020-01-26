node('jenkins-01') {

    currentBuild.result = "SUCCESS"

    slack_channel = 'jenkins'
    slack_message = ''
    slack_token_credential_id = '02'

    try {

        stage('Pull latest version from Gitlab'){

            slack_message = "Starting the Jenkins pipeline for config changes @ ${env.JOB_URL}"
            slackSend channel: "${slack_channel}", color: 'good', message: "${slack_message}", tokenCredentialId: "${slack_token_credential_id}"
            
            slack_message = "Pulling latest version of project from Gitlab"
            slackSend channel: "${slack_channel}", color: 'good', message: "${currentBuild.currentResult}: ${slack_message}", tokenCredentialId: "${slack_token_credential_id}"
            checkout scm

        }

        stage('Testing the build of Kafka Consumer Dockerfile'){

            sh 'make build_kafka_consumers'
            slack_message = 'Testing the build of Dockerfile'
            slackSend channel: "${slack_channel}", color: 'good', message: "${currentBuild.currentResult}: ${slack_message}", tokenCredentialId: "${slack_token_credential_id}"

        }

        stage('JSNAPy Tests'){

            slack_message = 'Calling Ansible Tower REST API to execute JSNAPy tests'
            slackSend channel: "${slack_channel}", color: 'good', message: "PENDING: ${slack_message}", tokenCredentialId: "${slack_token_credential_id}"

            ansiColor('xterm') {
                ansibleTower async: false, credential: '', extraVars: '', importTowerLogs: true, importWorkflowChildLogs: true, inventory: '', jobTags: '', jobTemplate: 'JSNAPy check: BGP neighbors', jobType: 'run', limit: 'router_pe', removeColor: false, skipJobTags: '', templateType: 'job', throwExceptionWhenFail: false, towerServer: 'Ansible AWX 9.0.1', verbose: false
            }

            ansiColor('xterm') {
                ansibleTower async: false, credential: '', extraVars: '', importTowerLogs: true, importWorkflowChildLogs: true, inventory: '', jobTags: '', jobTemplate: 'JSNAPy check: IS-IS Interfaces', jobType: 'run', limit: 'router_pe', removeColor: false, skipJobTags: '', templateType: 'job', throwExceptionWhenFail: false, towerServer: 'Ansible AWX 9.0.1', verbose: false
            }

        }

        stage('Send out completion message'){

            slackSend channel: "${slack_channel}", color: 'good', message: "${currentBuild.currentResult}: visit ${env.JOB_URL} for more details", tokenCredentialId: "${slack_token_credential_id}"

        }

    }
    catch (err) {

        currentBuild.result = "FAILURE"

            slackSend channel: "${slack_channel}", color: 'bad', message: "${currentBuild.currentResult}: visit ${env.JOB_URL} for more details", tokenCredentialId: "${slack_token_credential_id}"

        throw err
    }

}
