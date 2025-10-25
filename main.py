# myenv\Scripts\Activate.ps1 source myenv/bin/activate
# uvicorn main:app --reload

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from models import Product
import database_models
from database import engine, session
from sqlalchemy.orm import Session

app = FastAPI() # Instantiate FastAPI class

# load_dotenv()  # Already loaded .env file in database.py so no need to load again
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("WHITELIST_URL")], # To enable whitelist url to connect to backend
    allow_methods=["*"] # To allow CRUD methods making changes to the server
)


database_models.Base.metadata.create_all(bind=engine) # Create tables in db defined in database_models.py

# products = [
#     Product(id=1, name="Laptop", desc="Gaming Laptop", price=1200.0, qty=10),
#     Product(id=2, name="Mouse", desc="Wireless Mouse", price=25.5, qty=50),
#     Product(id=3, name="Keyboard", desc="Wireless Keyboard", price=60.0, qty=5)
# ]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# def init_db():  # to populate data on first load
#     db = session()
#     count = db.query(database_models.Product).count()

#     if count == 0:
#         for product in products:
#             db.add(database_models.Product(**product.model_dump()))
#         db.commit()

# init_db()

@app.get("/") # GET method - "/" is default homepage endpoint
def test():
    return 'hello world!'


@app.get('/products/')
def get_aLL_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get('/products/{id}')
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return 'product not found'


@app.post('/products/')
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product   


@app.put('/products/{id}')
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.desc = product.desc
        db_product.price = product.price
        db_product.qty = product.qty
        db.commit()
    else:
        return 'No product found'

@app.delete('/products/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else: 
        return 'No product found'


