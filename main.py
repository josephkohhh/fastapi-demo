from fastapi import FastAPI
from models import Product


app = FastAPI() # Instantiate FastAPI class

products = [
    Product(id=1, name="Laptop", desc="Gaming Laptop", price=1200.0, qty=10),
    Product(id=2, name="Mouse", desc="Wireless Mouse", price=25.5, qty=50)
]

@app.get("/") # GET method - "/" is default homepage endpoint
def test():
    return 'hello world!'

@app.get('/products')
def get_aLL_products():
    return products