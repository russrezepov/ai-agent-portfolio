import os
import faiss
import numpy as np
import ollama

docs = []
for file in os.listdir("docs"):
    with open(f"docs/{file}", "r", errors="ignore") as f:
        docs.append(f.read())

embeddings = [ollama.embeddings(model="llama3", prompt=d)["embedding"] for d in docs]

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings).astype("float32"))

while True:
    q = input("Ask a question: ")
    qe = ollama.embeddings(model="llama3", prompt=q)["embedding"]
    _, i = index.search(np.array([qe]).astype("float32"), 1)
    context = docs[i[0][0]]
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": f"Answer ONLY using this context:\n{context}\n\nQuestion: {q}"}]
    )
    print(response["message"]["content"])
