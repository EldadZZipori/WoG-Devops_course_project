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
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
           sh 'python --version'
           script{
            try {
            sh 'python3 e2e.py' 
           }
           catch(e){
            echo 'Mainscore test failed - see logs for more information'
            throw e
            
           } 
           }
           
        }
      }
    }

    stage('Finalize') {
      steps {
        echo '[+] Closing everything'
        dir('/Users/eldadzipori/Documents/GitHub/WoG-Devops_course_project'){
           sh 'docker-compose stop'
           sh 'docker-compose down'
        }
      }
    }

  }
}
