from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgres://postgres:P@ssw0rd@localhost:5432/fastapidemo"   
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)