pipeline {
    agent any
    
    parameters {
        string(name: 'KULLANICI_ADI', defaultValue: 'Muhammed', description: 'Gelistirici ismi')
    }

    stages {
        stage('Selamlama') {
            steps {
                echo "Merhaba ${params.KULLANICI_ADI}! Atomik gelisim devam ediyor."
            }
        }
        stage('Sistem Kontrolü') {
            steps {
                sh 'uptime'
            }
        }
    }
}pipeline {
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
