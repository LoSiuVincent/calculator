pipeline {
  agent {
    docker {
      image 'python:3.8-slim'
    }
  }
  
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    
    stage('Run Tests') {
      steps {
        sh 'pytest'
      }
    }
  }
}