import requests

OPENROUTER_API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "openrouter/openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "سلام"}
    ]
}

response = requests.post(url, headers=headers, json=payload)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
