pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo '[+] Checking out of version control'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
            checkout scm
        }
      }
    }

    stage('Build') {
      steps {
        echo '[+] Building Docker image from local Dockerfile'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
            sh 'docker build .'
        }
        
      }
    }

    stage('Run') {
      steps {
        echo '[+] Running Docker from local .yml file'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
           sh 'docker-compose up -d' 
        }
        
      }
    }

    stage('Test') {
      steps {
        echo '[+] Tesing MainScore with e2e.py'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project/tests'){
           sh 'python --version'     
           sh 'python3 e2e.py' 
        }
      }
    }
  }
  post {
    always {
        echo '[+] Closing everything'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
           sh 'docker-compose stop'
           sh 'docker-compose down'
        }
    }

    success {
      echo '[+] The pipeline ran successfully'
    }
    failure {
      echo '[-] The pipeline has failed'
    }
  }
}
