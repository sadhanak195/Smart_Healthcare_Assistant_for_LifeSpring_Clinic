import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

STORE = "vector_store.pkl"

def save_store(chunks):
    texts = [c["text"] for c in chunks]
    vec = TfidfVectorizer(stop_words="english")
    X = vec.fit_transform(texts)
    with open(STORE, "wb") as f:
        pickle.dump((vec, X, chunks), f)

def load_store():
    with open(STORE, "rb") as f:
        return pickle.load(f)
