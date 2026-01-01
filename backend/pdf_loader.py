import os
from pypdf import PdfReader

def load_pdfs(folder):
    docs = []
    for f in os.listdir(folder):
        if f.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder, f))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            docs.append({"source": f, "text": text})
    return docs
