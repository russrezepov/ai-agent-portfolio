import ollama

def analyze(customer):
    prompt = f"Analyze churn risk and key signals:\n{customer}"
    return ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])["message"]["content"]
