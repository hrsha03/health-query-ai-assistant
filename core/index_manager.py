import os
import faiss
import numpy as np
import pickle
from core.embedder import get_titan_embedding

STORAGE_DIR = "storage"
INDEX_FILE = os.path.join(STORAGE_DIR, "index.faiss")
EMBED_FILE = os.path.join(STORAGE_DIR, "embeddings.pkl")
DOC_FILE = os.path.join(STORAGE_DIR, "docs.pkl")

def build_or_load_index(folder="data"):
    if os.path.exists(INDEX_FILE) and os.path.exists(EMBED_FILE) and os.path.exists(DOC_FILE):
        print("✅ Loading cached FAISS index and embeddings...")
        index = faiss.read_index(INDEX_FILE)
        with open(EMBED_FILE, "rb") as f:
            embeddings = pickle.load(f)
        with open(DOC_FILE, "rb") as f:
            docs = pickle.load(f)
        return index, docs

    print("🛠 Building index from scratch (first-time setup)...")
    docs = []
    vectors = []

    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            path = os.path.join(folder, fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                docs.append(content)
                emb = get_titan_embedding(content[:1000])  # Avoid 8k token limits
                vectors.append(emb.astype('float32'))

    embeddings = np.array(vectors)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # Save everything for reuse
    faiss.write_index(index, INDEX_FILE)
    with open(EMBED_FILE, "wb") as f:
        pickle.dump(embeddings, f)
    with open(DOC_FILE, "wb") as f:
        pickle.dump(docs, f)

    return index, docs
