from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["ai_telegram_bot"]

# collections
users_collection = db["users"]
messages_collection = db["messages"]
