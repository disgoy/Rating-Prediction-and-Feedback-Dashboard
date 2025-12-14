import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Feedback System"
}

data = {
    "model": "mistralai/mistral-7b-instruct",
    "messages": [
        {"role": "user", "content": "Reply politely to a customer who gave a 2-star review"}
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result["choices"][0]["message"]["content"])