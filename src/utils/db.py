from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/gyk1nordwinds"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI için dependency olarak kullanılabilir
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""" 
# Bağlantıyı test et
try:
    with engine.connect() as connection:
        print("PostgreSQL bağlantısı başarılı!")
except Exception as e:
    print("Bağlantı hatası:", e)

query = "SELECT * FROM orders LIMIT 5;"
df = pd.read_sql(query, engine)

print(df)"""