from database.mongo import users_collection
from datetime import datetime, timedelta

MAX_REQUESTS_PER_DAY = 30

async def check_and_update_limit(user_id):
    user = await users_collection.find_one({"user_id": user_id})
    now = datetime.utcnow()
    
    # ریست محدودیت اگر روز جدید شروع شده
    if user["last_reset"] < now - timedelta(days=1):
        await users_collection.update_one({"user_id": user_id}, {
            "$set": {"requests_today": 1, "last_reset": now}
        })
        return True

    if user["requests_today"] < MAX_REQUESTS_PER_DAY:
        await users_collection.update_one({"user_id": user_id}, {
            "$inc": {"requests_today": 1}
        })
        return True
    
    return False
