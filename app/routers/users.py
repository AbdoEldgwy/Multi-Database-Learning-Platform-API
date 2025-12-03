from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import SessionLocal
from app.models.user import User
from pydantic import BaseModel, EmailStr
from sqlalchemy import insert, select
from utils.hashing_pwd import hash_password, verify_password
from app.logs.Log_it import log_auth

router = APIRouter()

class SessionData():
    metadata: dict = {"ip": "127.0.0.1", 
                    "user_agent": "Mozilla/5.0", 
                    "token": "eyJhbGciOiJIUzI1NiIsInR"} # Example metadata

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == user.email)
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        action_state = "Failed_registration"
        await log_auth(user_id=str(existing_user.id), action=action_state, metadata=SessionData.metadata) # type: ignore
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    stmt = insert(User).values(
        name=user.name,
        email=user.email,
        password=hashed_password
    ).returning(User)
    result = await db.execute(stmt)
    await db.commit()

    new_user = result.scalar_one()
    action_state = "Successful_registration"
    await log_auth(user_id=str(new_user.id), action=action_state, metadata=SessionData.metadata) # type: ignore
                                                                                   
    return new_user


class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == user.email)
    result = await db.execute(stmt)
    user_db = result.scalar_one_or_none()
    
    if not user_db:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    print(f"user_db----------: {user_db.email}")
    if not verify_password(user.password, user_db.password): # type: ignore
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful"}


@router.get("/all", response_model=list[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    stmt = select(User)
    result = await db.execute(stmt)
    users = result.scalars().all()
    return users

@router.get("/id/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
