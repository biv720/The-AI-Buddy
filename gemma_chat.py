import os
import requests
from dotenv import load_dotenv

# Load API key from .env (best practice)
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(prompt, model="mistralai/mistral-7b-instruct:free"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # required by OpenRouter policy
    }

    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a compassionate mental health assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=body, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("🧠 You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            break
        reply = get_ai_response(user_input)
        print("🤖 Mistral:", reply)
