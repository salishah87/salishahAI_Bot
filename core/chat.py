import requests
from config import OPENROUTER_API_KEY

def ask_openrouter(prompt: str, user_id: int) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",  # اختیاری، اما OpenRouter توصیه کرده
        "X-Title": "Telegram AI Bot"              # برای ریت‌لیمیت بهتر
    }

    data = {
        "model": "openrouter/openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"❌ API Error {response.status_code}: {response.text}")
        raise Exception("خطا در اتصال به مدل.")
