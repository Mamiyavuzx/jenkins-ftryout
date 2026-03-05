pipeline {
    agent any

    stages {
        stage('Atomik Kontrol') {
            steps {
                echo 'Sistem her gun %1 gelisiyor...'
            }
        }
        stage('Sistem Bilgisi') {
            steps {
                // Burada Debian sisteminden bir bilgi cekelim
                sh 'uptime'
                sh 'free -m'
            }
        }
    }
    
    post {
        success {
            echo 'Harika! Aliskanlik zinciri kirilmadi, basariyla tamamlandi.'
        }
        failure {
            echo 'Dikkat! Bir hata olustu, sistemi kontrol et.'
        }
    }
}
