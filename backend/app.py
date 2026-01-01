from flask import Flask, request, jsonify
from flask_cors import CORS
from vector_store import load_store
from answer_generator import generate_answer
from metrics import metrics
import numpy as np

app = Flask(__name__)
CORS(app)

vec, X, chunks = load_store()

@app.route("/chat", methods=["POST"])
def chat():
    q = request.json["query"]
    start = metrics.start()

    qv = vec.transform([q])
    scores = (X @ qv.T).toarray().ravel()
    top = scores.argsort()[-3:][::-1]

    retrieved = [chunks[i] for i in top]
    ans = generate_answer(q, retrieved, scores[top])


    metrics.end(start)
    return jsonify({"answer": ans})

app.run(port=5000, debug=True)
