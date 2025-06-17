from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["telegram_ai_bot"]

# دسترسی به کالکشن‌ها
chat_collection = db["chats"]
user_collection = db["users"]
