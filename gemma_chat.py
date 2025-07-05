import os
from llama_cpp import Llama

# Dynamically locate the model file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.gguf")

# Load the model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, verbose=False)

def get_ai_response(prompt):
    formatted_prompt = (
        "<start_of_turn>user\n"
        f"{prompt}\n"
        "<end_of_turn>\n"
        "<start_of_turn>model\n"
    )
    response = llm(formatted_prompt, max_tokens=256, stop=["<end_of_turn>"])
    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("🧠 You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            break
        reply = get_ai_response(user_input)
        print("🤖 Gemma:", reply)
