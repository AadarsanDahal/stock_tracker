from pydantic import BaseModel

class product(BaseModel): 
    id : int
    name : str
    description : str
    quantity : int
    price : float

 


