import hashlib
import numpy as np

def embed(text, dim=384):
    h = hashlib.sha256(text.encode()).digest()
    v = np.frombuffer(h, dtype=np.uint8).astype(float)
    return np.pad(v, (0, dim - len(v)))
