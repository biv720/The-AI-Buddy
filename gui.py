import tkinter as tk
from tkinter import scrolledtext
from gemma_chat import get_ai_response
from voice_input import get_voice_input
from tts import speak

def send_message():
    user_input = input_box.get()
    if not user_input.strip():
        return

    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_input}\n")
    input_box.delete(0, tk.END)

    ai_response = get_ai_response(user_input)
    chat_window.insert(tk.END, f"Gemma: {ai_response}\n\n")
    chat_window.config(state='disabled')
    chat_window.yview(tk.END)
    speak(ai_response)

def speak_input():
    user_input = get_voice_input()
    input_box.delete(0, tk.END)
    input_box.insert(0, user_input)
    send_message()

def clear_chat():
    chat_window.config(state='normal')
    chat_window.delete('1.0', tk.END)
    chat_window.config(state='disabled')

# UI Setup
root = tk.Tk()
root.title("AI Therapy - Gemma Edition 🧠")
root.geometry("600x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Segoe UI", 10))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_box = tk.Entry(input_frame, width=50, font=("Segoe UI", 11))
input_box.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

voice_button = tk.Button(input_frame, text="🎤 Speak", command=speak_input)
voice_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="🧹 Clear Chat", command=clear_chat)
clear_button.pack(pady=5)

root.mainloop()
