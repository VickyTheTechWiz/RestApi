from fastapi import FastAPI, Path
from typing import Optional 
from pydantic import BaseModel
from pydantic import BaseModel, validator
from fastapi import Depends, HTTPException


app = FastAPI()

products = {
    1: {
        "name": "Selena ware",
        "category": "glass"
    }
}

class Product(BaseModel):
    name: str
    category: str
    

class UpdateProduct(BaseModel):
     name: Optional[str] = None
     category:  Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-product/{product_id}")
def get_product(product_id: int = Path(None, description="The ID of the product you want to view", gt=0, lt=3)):
    return products[product_id]

@app.get("/get-by-name/{product-id}")
def get_product(*, product_id: int, name : Optional[str] = None, test : int):
    for product_id in products:
        if products[product_id]["name"] == name:
            return products[product_id]
    return{"Data": "Not found"}        

@app.post("/create-product/{product_id}")
def create_product(product_id : int, product : Product):
    if product_id in products:
        return {"Error": "Product exists"}

    if products[product_id] == products:
        return products[product_id]

@app.put("/update-product/{product_id}")
def update_product(product_id: int, product: UpdateProduct): 
    if product_id not in products:
        return {"Error": "Product does not exist"}
        
    if product.name != None:
        products[product_id].name = product.name
        return products[product_id]

    if product.category != None:
        products[product_id].category = product.category

        return products[product_id]

@app.delete("/delete-product/{product_id}")
def delete_product(product_id: int ):
     if product_id not in products:
         return {"Error": "Product does not exist" }

     del products[product_id]
     return {"Message": "Product deleted successfully"}