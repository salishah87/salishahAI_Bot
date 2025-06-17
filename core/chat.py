import requests
from config import OPENROUTER_API_KEY

class ChatModule:
    def __init__(self):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

    def send_message(self, user_message):
        payload = {
            "model": "openrouter/openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": user_message}
            ]
        }
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            # استخراج پاسخ از ساختار بازگشتی OpenRouter
            return data['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as http_err:
            return f"❌ خطا در اتصال به مدل: {http_err}"
        except Exception as err:
            return f"❌ خطای نامشخص: {err}"
