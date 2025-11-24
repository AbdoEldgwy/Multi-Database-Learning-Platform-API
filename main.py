from fastapi import FastAPI
from app.db.init_db import init_db
from app.routers.users import router as user_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working!"}

app.include_router(user_router, prefix="/users")

@app.on_event("startup")
async def startup_event():
    await init_db()
