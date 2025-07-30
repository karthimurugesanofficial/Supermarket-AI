import requests
import json
from config import OPENROUTER_API_KEY, LLM_MODEL

def query_deepseek(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "You are an AI assistant for a supermarket. Use only the given product data."},
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": LLM_MODEL,
        "messages": messages
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['choices'][0]['message']['content']
