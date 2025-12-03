from app.db.mongo import db
from app.models.mongo_models import SessionLog
from datetime import datetime

async def log_auth(user_id: str, action: str, metadata: dict):  
    log_entry = SessionLog(
        user_id=user_id,
        action=action,
        metadata=metadata,
        timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    log_dict = log_entry.model_dump()
    await db['auth_logs'].insert_one(log_dict)

# import asyncio
# asyncio.run(log_auth_action("12345", "login", {"ip": "192.168.1.1"}))