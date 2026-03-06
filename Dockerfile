# Temel imaj olarak hafif bir Python seçiyoruz
FROM python:3.9-slim

# Çalışma dizinini belirliyoruz
WORKDIR /app

# Kodumuzu konteynerin içine kopyalıyoruz
COPY merhaba.py .

# Konteyner çalıştığında ne yapacağını söylüyoruz
CMD ["python", "merhaba.py"]
