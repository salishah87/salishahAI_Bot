from db.connection import chat_collection
from datetime import datetime

def save_chat(user_id: int, prompt: str, response: str):
    chat_collection.insert_one({
        "user_id": user_id,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.utcnow()
    })
