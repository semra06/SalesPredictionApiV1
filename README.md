# SalesPredictionApiV1

 Satış Tahmini API Projesi

Northwind Verisi ile Ürün Bazlı Satış Tahminleme ve API Geliştirme
Python | FastAPI | scikit-learn | PostgreSQL | Swagger | SQLAlchemy

🎯 Proje Amacı

Bu projenin temel amacı, Northwind veritabanındaki satış verilerini kullanarak ürün bazlı satış tahminlemesi yapan bir makine öğrenmesi modeli geliştirmek ve bu modeli RESTful API aracılığıyla dış sistemlere sunmaktır.
🧰 Kullanılan Teknolojiler
Alan 	Teknoloji
💻 Programlama 	Python 3.x
⚙️ API Framework 	FastAPI
🛢️ Veritabanı 	PostgreSQL
🔗 ORM 	SQLAlchemy
🧠 Makine Öğrenmesi 	scikit-learn
📊 Veri İşleme 	pandas, numpy
💾 Model Kaydetme 	joblib
📘 Dokümantasyon 	Swagger (FastAPI)
🧪 Test ve Ara Yüz 	Swagger UI / Postman
📁 Proje Yapısı

SalesPredictionApiV1/
│
├── main.py                        # FastAPI ana uygulaması
├── requirements.txt               # Proje bağımlılıkları
├── {model_name}_model.pkl         # Eğitilmiş model dosyaları
├── processed_data.csv             # Temizlenmiş ve işlenmiş veri seti
├── product_sales_summary.csv      # Ürün bazlı özet veriler
├── monthly_sales_summary.csv      # Aylık satış özetleri
│
└── src/
    ├── model/
    │   └── model.py               # Model eğitimi ve tahmin fonksiyonları
    ├── utils/
    │   └── data_fetch.py          # SQL sorguları ve veri çekme
    ├── development/
    │   └── data_manipulation.py  # Özellik mühendisliği ve veri ön işleme
    └── schemas.py                # FastAPI veri şemaları (pydantic)

🔍 Proje Akışı
A. Veri Tabanı ve Veri İşleme

    PostgreSQL üzerinde Northwind veritabanı kuruldu
    Orders, Order_Details, Products, Customers tabloları analiz edildi
    SQLAlchemy ile veriler çekildi
    Pandas ile veri temizliği ve işlenmesi yapıldı
    Aylık ve ürün bazlı özet CSV'ler üretildi
    Özellik mühendisliği (ay, fiyat, segment vs.)

B. Modelleme

    Hedef değişken: Ürün bazlı satış miktarı
    Eğitim/test ayrımı (train_test_split)
    Model: Basit regresyon modeli (Linear Regression / RandomForest)
    Başarı metrikleri: R², RMSE
    Model joblib ile {model_name}_model.pkl olarak kaydedildi

C. API Geliştirme

FastAPI kullanılarak geliştirilen bu RESTful API, ürün listeleme, fiyat tahmini, satış özetleri sunumu, modelin yeniden eğitilmesi ve model görselleştirmelerine erişim gibi temel işlevleri kapsamaktadır.
Endpoint 	Yöntem 	Açıklama
/products 	GET 	Veritabanında kayıtlı tüm ürünleri JSON formatında listeler.
/predict 	POST 	Kullanıcıdan alınan ürün, müşteri ve tarih bilgilerine göre tahmini fiyat çıktısı döner.
/sales_summary 	GET 	Aylık ve ürün bazlı satış özetlerini ve bu özetlere ait görselleri döndürür.
/retrain 	POST 	Seçilen algoritmaya göre modeli güncel verilerle yeniden eğitir ve yeni modeli kayıt eder.
/visualizations 	GET 	Eğitilen modele ait kayıtlı görselleştirmeleri listeler.

2025-04-07_14-16-29
🔹 /retrain Endpoint'i Detaylandırması

/retrain uç noktası, seçilen makine öğrenmesi algoritmasını kullanarak modeli yeniden eğitir. Bu, modelin güncel verilerle daha doğru sonuçlar üretmesini sağlar.

    Yöntem: POST
    Query Parametresi:
        model_name: LinearRegression, DecisionTree, KNN (zorunlu)
    İşleyiş Adımları:
        API, ilgili veriyi DataFetch sınıfı ile çeker.
        Veriler DataManipulation modülü ile işlenir.
        Seçilen model eğitilir ve başarı metrikleri hesaplanır.
        Yeni model best_model.pkl, kullanılan özellikler feature_columns.pkl olarak kaydedilir.

2025-04-07_14-17-29 2025-04-07_14-18-08
API'yi Çalıştırma
1. Bağımlılıkları Kur

pip install -r requirements.txt

2. API'yi Başlat

uvicorn main:app --reload

Test Süreci

    Swagger UI ile uç noktalar test edildi
    Postman üzerinden örnek istekler gönderildi
    Hatalı veri validasyonu test edildi (pydantic)
    Response kodları: 200, 422, 500 yönetildi

2025-04-07_14-17-03
📦 Docker (Opsiyonel)

FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

📚 İlham Kaynağı & API Referansı

    Northwind Database 📎
    Swagger UI
    Hepsiburada API Örneği 📎

📌 Projenin Güçlü Yanları

    ✔️ Gerçek veritabanı entegrasyonu
    ✔️ End-to-end modelleme ve dağıtım
    ✔️ Swagger üzerinden kolay test imkanı
    ✔️ Temiz ve modüler kod yapısı

✍️ Geliştirici

    Merve
    GitHub • LinkedIn
    📬 İletişim için: merveacar.ce@gmail.com

📝 Lisans

MIT © 2025
