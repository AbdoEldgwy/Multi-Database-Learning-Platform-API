from pydantic import BaseModel

class MongoProduct(BaseModel):  
    name: str
    description: str 
    price: int

# ----

class SessionLog(BaseModel):
    user_id: str
    action: str
    metadata: dict
    timestamp: str