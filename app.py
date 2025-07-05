from flask import Flask, request, render_template, send_file
from gtts import gTTS
from gemma_chat import get_ai_response
from tts import speak
import uuid
import os

app = Flask(__name__)
chat_history = []


@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    global chat_history
    audio_file = None

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            response = get_ai_response(user_input)
            audio_file = speak(response)

            # Add both user and Gemma messages to history
            chat_history.append({"sender": "user", "text": user_input})
            chat_history.append({"sender": "ai", "text": response, "audio": audio_file})

    return render_template("index.html", chat_history=chat_history)


    return render_template("index.html")

if __name__ == "__main__":
    import os
    os.environ['FLASK_RUN_FROM_CLI'] = 'false'  # Prevents Click banner/logs
    app.run(debug=False)
