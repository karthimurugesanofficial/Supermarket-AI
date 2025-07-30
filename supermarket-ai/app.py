import os
import requests
from flask import Flask, request
from dotenv import load_dotenv
from rag_engine import get_smart_reply

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

user_chat_history = {}
MAX_HISTORY = 5

app = Flask(__name__)

@app.route("/telegram", methods=["POST"])
def telegram_reply():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        incoming_msg = data["message"].get("text", "")
        user_id = str(chat_id)

        # Maintain user history
        user_chat_history.setdefault(user_id, []).append({"role": "user", "content": incoming_msg})
        user_chat_history[user_id] = user_chat_history[user_id][-MAX_HISTORY:]

        reply = get_smart_reply(user_chat_history[user_id])
        user_chat_history[user_id].append({"role": "assistant", "content": reply})
        user_chat_history[user_id] = user_chat_history[user_id][-MAX_HISTORY:]

        requests.post(TELEGRAM_API, json={"chat_id": chat_id, "text": reply})

    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))  # Change default to 8080
    app.run(host="0.0.0.0", port=port)


