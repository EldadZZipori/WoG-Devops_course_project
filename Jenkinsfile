pipeline {
 agent: any
 
 stages {		
  stage('Checkout') {
   echo '[+] Checking out source control'
   checkout: scm
  }

  stage('Build') {
   echo '[+] Building Docker image from local Dockerfile'
   sh 'docker build .'
  }

  stage('Run') {
   echo '[+] Running Docker from local .yml file'
   sh 'docker-compose up'
  }

  stage('Test') {
   echo '[+] Tesing MainScore with e2e.py"
   didFail = sh 'python e2e.py'
  }

  stage('Finalize') {
   echo '[+] Closing everything'
   sh 'docker-compose stop'
  }
 }
}
