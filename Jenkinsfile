pipeline {
    agent any
    
    environment {
        // Docker Hub kullanıcı adını buraya yaz
        DOCKER_USER = 'senin_kullanici_adin'
        IMAGE_NAME = 'mami-proje-w'
    }

    stages {
        stage('Test ve Kontrol') {
            steps {
                echo 'Kod doğrulaniyor...'
                sh 'python3 merhaba.py'
            }
        }
        stage('Docker Paketleme') {
            steps {
                echo 'Imaj olusturuluyor...'
                sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER} ."
                sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:latest ."
            }
        }
        stage('Docker Hub\'a Gönder (Push)') {
            steps {
                echo 'Imaj kütüphaneye gönderiliyor...'
                // NOT: Burada Jenkins Credentials kullanarak login olman gerekecek
                sh "docker login -u ${DOCKER_USER} -p 'SENIN_DOCKER_TOKEN_VEYA_SIFREN'"
                sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:latest"
            }
        }
    }
}
