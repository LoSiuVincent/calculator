pipeline {
  agent any
  
  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt --break-system-packages'
      }
    }
    
    stage('Run Tests') {
      steps {
        sh 'python3 -m pytest'
      }
    }
  }
}