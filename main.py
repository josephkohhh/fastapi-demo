# myenv\Scripts\Activate.ps1
# uvicorn main:app --reload

from fastapi import FastAPI
from models import Product


app = FastAPI() # Instantiate FastAPI class

products = [
    Product(id=1, name="Laptop", desc="Gaming Laptop", price=1200.0, qty=10),
    Product(id=2, name="Mouse", desc="Wireless Mouse", price=25.5, qty=50),
    Product(id=3, name="Keyboard", desc="Wireless Keyboard", price=60.0, qty=5)
]

@app.get("/") # GET method - "/" is default homepage endpoint
def test():
    return 'hello world!'

@app.get('/products')
def get_aLL_products():
    return products

@app.get('/product/{id}')
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return 'product not found'


@app.post('/product')
def add_product(product: Product):
    products.append(product)
    return product   


@app.put('/product')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return 'product updated successfully'
        
    return 'No product found'


@app.delete('/product')
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]  # Removes by index, which is precise and faster
            return 'product deleted successfully'
    return 'No product found'
