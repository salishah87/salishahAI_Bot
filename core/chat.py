import requests
from config import OPENROUTER_API_KEY

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openrouter/openai/gpt-3.5-turbo",
        "messages": messages
    }
    response = requests.post(OPENROUTER_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"❌ خطا در اتصال به مدل: {response.status_code} {response.text}")
