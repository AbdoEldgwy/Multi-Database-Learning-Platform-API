from motor.motor_asyncio import AsyncIOMotorClient
from config import Settings

MONGO_URL = Settings().MONGO_URI

client = AsyncIOMotorClient(MONGO_URL)
db = client["learn_db"] 