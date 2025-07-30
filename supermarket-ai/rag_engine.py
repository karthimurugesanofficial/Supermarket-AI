from utils import load_product_data, row_to_text
from embeddings import get_embeddings
from vectordb import VectorStore
from prompt_builder import build_prompt
from llm_interface import query_deepseek
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("❌ OPENROUTER_API_KEY not loaded!")

def get_smart_reply(history):
    print("🧠 get_smart_reply called with chat history:", history)

    try:
        from vector_search import search_top_k
        import pandas as pd  # Only needed here

        query = history[-1]['content']
        df = pd.read_csv("data/Supermarket - Sheet1.csv")

        context = search_top_k(query, df, k=3)
        print("🔍 Retrieved context:", context)

        # Construct prompt
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant for a supermarket."},
            *history,
            {"role": "system", "content": f"Context:\n{context}"}
        ]

        return get_llm_response(messages)

    except Exception as e:
        print("❌ Error in get_smart_reply:", e)
        return "Sorry, I couldn’t process that. Please try again."


    
import requests
import json
import os

from config import OPENROUTER_API_KEY


def get_llm_response(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",  # ✅ try without the slash
        "messages": messages
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("📡 LLM Status Code:", response.status_code)
    print("📦 LLM Raw Response:", response.text)  # 🔍 This is what we need to see

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ LLM error:", e)
        return "Sorry, something went wrong with the AI model."




