pipeline {
    agent any

    tools {
        maven 'M3'     // Replace with your Maven tool name in Jenkins
        jdk 'JDK11'    // Replace with your JDK tool name in Jenkins
    }

    environment {
        WLST_PATH    = '/u01/data/middleware/oracle_common/common/bin/wlst.sh'
        ADMIN_URL    = 't3://172.31.41.166:7001'
        ADMIN_USER   = 'weblogic'
        ADMIN_PASS   = 'weblogic123'
        APP_NAME     = 'mybank'
        WAR_PATH     = 'target/mywebapp.war'
        CLUSTER_NAME = 'DemoCluster'
        SCRIPT       = 'deploy.py'
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build WAR') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Deploy to WebLogic Cluster') {
            steps {
                sh """
                ${WLST_PATH} ${SCRIPT} ${ADMIN_URL} ${ADMIN_USER} ${ADMIN_PASS} ${WAR_PATH} ${APP_NAME} ${CLUSTER_NAME}
                """
            }
        }
    }
}


