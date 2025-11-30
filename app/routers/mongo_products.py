from fastapi import APIRouter, HTTPException
from app.db.mongo import db
from app.models.mongo_product import MongoProduct
from bson import ObjectId

router = APIRouter()

@router.post("/mongo/products/")
async def create_product(product: MongoProduct):
    product_dict = product.model_dump()
    result = await db['products'].insert_one(product_dict) # insert_one returns result with inserted_id "_id"
    product_dict["_id"] = str(result.inserted_id)
    return product_dict

# --- Get all ---
@router.get("/mongo/products")
async def list_mongo_products():
    products = []
    cursor = db['products'].find()
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        products.append(doc)
    return products


# --- Get one ---
@router.get("/mongo/products/{product_id}")
async def get_mongo_product(product_id: str):
    doc = await db['products'].find_one({"_id": ObjectId(product_id)})
    if not doc:
        raise HTTPException(404, "Product not found")
    
    doc["_id"] = str(doc["_id"])
    return doc
