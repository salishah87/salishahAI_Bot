from database.mongo import users_collection, messages_collection
from datetime import datetime

async def register_user(user_id, username):
    user = await users_collection.find_one({"user_id": user_id})
    if not user:
        await users_collection.insert_one({
            "user_id": user_id,
            "username": username,
            "requests_today": 0,
            "last_reset": datetime.utcnow()
        })

async def log_message(user_id, message, response):
    await messages_collection.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response,
        "timestamp": datetime.utcnow()
    })
