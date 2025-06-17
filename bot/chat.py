import requests
from config import OPENROUTER_API_KEY

async def handle_message(update, context):
    user_text = update.message.text
    response_text = await ask_openrouter(user_text)

    await update.message.reply_text(response_text)

async def ask_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ خطا در اتصال به مدل: {e}"

