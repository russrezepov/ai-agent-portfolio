import ollama

def plan(analysis):
    prompt = f"Based on analysis, decide next actions:\n{analysis}"
    return ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])["message"]["content"]
