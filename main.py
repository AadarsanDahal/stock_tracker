from fastapi import FastAPI
from models import product


app = FastAPI() # Create a FastAPI instance


#GET : Read
#Post : Create 
#put : Update
#Delete : Delete

products_list = [

product(id=1, name="Product 1", description="Description of Product 1", quantity=10, price=9.99),
product(id=2, name="Product 2", description="Description of Product 2", quantity=5, price=19.99),
product(id=3, name="Product 3", description="Description of Product 3", quantity=15, price=29.99)

] #List to store products


def greet(): #Define a function to return a greeting message
    return "Hello,Welcome to the stock tracker app!"

def products(): #Define a function to return a list of products
    return products_list 

def error_404(): #Define a function to return a 404 error message
    return "Product not found"


@app.get("/")   #GET  / -- home page ma 
def read_root():
    return greet()

@app.get("/products")  #GET /products -- list all products
def list_products():
    return products()


@app.get("/products/{product_id}")  
def get_product_by_id(product_id: int): #Define a function to get a product by its ID
    for product in products_list:
        if product.id == product_id:
            return product
    return error_404()


@app.post("/products")  #POST /products -- create a new product
def create_product(product: product):
    products_list.append(product)
    return product


#updating a product
@app.put("/products/{product_id}")  #PUT /products/{product_id} -- update a product by its ID
def update_product(product_id: int, updated_product: product):
    for i in range(len(products_list)):
        if products_list[i].id == product_id:
            products_list[i] = updated_product
            return updated_product
    return error_404()


#delete a procudt 
@app.delete("/products/{product_id}")  #DELETE /products/{product_id} -- delete a product by its ID
def delete_product(product_id: int):
    for i in range (len(products_list)):
        if products_list[i].id == product_id:
            deleted_product = products_list.pop(i)
            return deleted_product
    return error_404()

