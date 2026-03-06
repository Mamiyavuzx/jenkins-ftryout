pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Kalite kontrol yapiliyor...'
                sh 'python3 merhaba.py'
            }
        }
        stage('Docker Paketleme (Build Image)') {
            steps {
                echo 'Yazilim paketleniyor...'
                // 'proje-w' adında bir imaj oluşturuyoruz
                sh 'docker build -t mami-proje-w:latest .'
            }
        }
        stage('Paketi Kontrol Et') {
            steps {
                echo 'Olusturulan paketler listeleniyor...'
                sh 'docker images | grep mami-proje-w'
            }
        }
    }
}
