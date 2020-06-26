pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo '[+] Checking out of version control'
        git './'
      }
    }

    stage('Build') {
      steps {
        echo '[+] Building Docker image from local Dockerfile'
        sh 'sh \'docker build .\''
      }
    }

    stage('Run') {
      steps {
        echo '[+] Running Docker from local .yml file'
        sh 'sh \'docker-compose up\''
      }
    }

    stage('Test') {
      steps {
        echo '[+] Tesing MainScore with e2e.py'
        sh 'sh \'python e2e.py\''
      }
    }

    stage('Finalize') {
      steps {
        echo '[+] Closing everything'
        sh 'sh \'docker-compose stop\''
      }
    }

  }
}