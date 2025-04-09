# Python resmi imajı ile başla
FROM python:3.10-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Uygulamayı çalıştır
CMD ["python", "app.py"]
