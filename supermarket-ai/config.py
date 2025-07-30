import os
from dotenv import load_dotenv

load_dotenv()
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    print("❌ OPENROUTER_API_KEY is not set!")

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "deepseek/deepseek-chat"

