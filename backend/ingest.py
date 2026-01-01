from pdf_loader import load_pdfs
from chunker import chunk_texts
from vector_store import save_store

DATA_PATH = "../data"

if __name__ == "__main__":
    print("📄 Loading clinic PDFs...")
    documents = load_pdfs(DATA_PATH)

    print("✂️ Chunking documents...")
    chunks = chunk_texts(documents)

    print("💾 Saving vector store...")
    save_store(chunks)

    print("✅ Clinic PDFs indexed successfully")
