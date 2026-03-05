pipeline {
    agent any
    stages {
        stage('Sistem Kontrol') {
            steps {
                // Python'un yüklü olup olmadığını ve nerede olduğunu kontrol edelim
                sh 'which python3 || echo "Python bulunamadi"'
                sh 'ls -l'
            }
        }
        stage('Calistirma') {
            steps {
                // Dosya adının 'merhaba.py' ile tam eşleştiğinden emin ol
                sh 'python3 merhaba.py || echo "Calistirma sirasinda hata olustu"'
            }
        }
    }
}
