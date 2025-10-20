from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    desc: str
    price: float
    qty: int

    # Pydantic BaseModel will take care of the constructor
    # def __init__(self, id: int, name: str, desc: str, price: float, qty: int):
    #     self.id = id        
    #     self.name = name    
    #     self.desc = desc    
    #     self.price = price  
    #     self.qty = qty     

            
class Category:
    pass

class Order:
    pass

class User:
    pass