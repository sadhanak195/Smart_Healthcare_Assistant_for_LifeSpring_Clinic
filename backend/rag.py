import requests, os
import numpy as np
from vector_store import load
from metrics import metrics

HF_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

vectorizer, X, chunks = load()

def generate(query):
    metrics.requests += 1
    qv = vectorizer.transform([query])
    scores = np.dot(X, qv.T).toarray().flatten()
    top = scores.argsort()[-3:][::-1]

    if scores[top[0]] < 0.1:
        metrics.fallbacks += 1
        return "⚠️ Please contact Lifespring Clinic directly for accurate medical advice."

    context = "\n".join(chunks[i]["text"] for i in top)

    prompt = f"""
You are Lifespring Clinic Assistant.
Answer ONLY using the context.

Context:
{context}

Question:
{query}

Answer:
"""

    r = requests.post(HF_URL, headers=HEADERS, json={"inputs": prompt})
    return r.json()[0]["generated_text"]
