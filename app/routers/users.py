from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import SessionLocal
from app.models.user import User
from pydantic import BaseModel
from sqlalchemy import insert

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    stmt = insert(User).values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    await db.execute(stmt)
    await db.commit()
    return {"message": "User registered successfully!"}
