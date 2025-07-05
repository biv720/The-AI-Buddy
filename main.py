from gemma_chat import get_ai_response
from voice_input import get_voice_input
from tts import speak

while True:
    mode = input("Type 't' for text, 'v' for voice, or 'q' to quit: ")

    if mode == 'q':
        break

    if mode == 't':
        user_input = input("🤍You: ")
    elif mode == 'v':
        user_input = get_voice_input()
        print("You (voice):", user_input)
    else:
        print("Invalid input")
        continue

    response = get_ai_response(user_input)
    print("🤖 AI Buddy:", response)
    speak(response)

