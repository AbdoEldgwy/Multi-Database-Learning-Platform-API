from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.db.postgres import SessionLocal
from app.models.product import Product
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/publish", response_model=ProductResponse)
async def publish_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    new_product = Product(
        name = product.name,
        description = product.description,
        price = product.price
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product