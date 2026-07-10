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
    #postgress bt(a called stuff goes here 
    return products_list 


@app.get("/")   #GET  / -- home page ma 
def read_root():
    return greet()

@app.get("/products")  #GET /products -- list all products
def list_products():
    return products()



