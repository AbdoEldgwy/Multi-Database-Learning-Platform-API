from pydantic import BaseModel

class MongoProduct(BaseModel):  
    name: str
    description: str 
    price: int