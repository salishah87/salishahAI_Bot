import httpx
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def get_ai_response(prompt: str, user_id: int) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openrouter/mistral-7b",
        "messages": [{"role": "user", "content": prompt}]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        return response.json()["choices"][0]["message"]["content"]
