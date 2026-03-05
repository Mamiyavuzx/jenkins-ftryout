pipeline {
    agent any
    stages {
        stage('Kod Kontrol') {
            steps {
                echo 'GitHub\'dan Python dosyasi kontrol ediliyor...'
                sh 'ls -l'
            }
        }
        stage('Calistirma') {
            steps {
                // Debian sistemindeki python3'ü kullanarak dosyayı çalıştırıyoruz
                sh 'python3 merhaba.py'
            }
        }
    }
}
