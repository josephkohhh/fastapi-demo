from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base() # Instantiate base class

class Product(Base):

    __tablename__ = 'product' # db table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    desc = Column(String)
    price = Column(Float)
    qty = Column(Integer)  