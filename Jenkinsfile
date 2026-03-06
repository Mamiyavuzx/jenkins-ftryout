pipeline {
    agent any
    stages {
        stage('Derleme ve Kontrol') {
            steps {
                echo 'Dosyalar kontrol ediliyor...'
                sh 'ls -l'
            }
        }
        stage('Unit Test (Birim Deneyi)') {
            steps {
                echo 'Matematiksel tutarlilik testi baslatiliyor...'
                // Python kodunu calistiriyoruz, eger exit(1) dönerse Jenkins bu stage'i durdurur
                sh 'python3 merhaba.py'
            }
        }
        stage('Yayinlama (Deployment)') {
            steps {
                echo 'Test basarili! Yazilim dunyaya sunulmaya hazir.'
            }
        }
    }
    post {
        failure {
            echo 'KRITIK HATA: Matematiksel tutarlilik saglanamadi! Zincir kirildi.'
        }
    }
}
