import os
import faiss
import numpy as np
import pickle
from core.embedder import get_titan_embedding

STORAGE_DIR = "storage"
INDEX_FILE = os.path.join(STORAGE_DIR, "index.faiss")
EMBED_FILE = os.path.join(STORAGE_DIR, "embeddings.pkl")
DOC_FILE = os.path.join(STORAGE_DIR, "docs.pkl")
FILEMAP_FILE = os.path.join(STORAGE_DIR, "filenames.pkl")


def build_or_load_index(folder="data"):
    os.makedirs(STORAGE_DIR, exist_ok=True)

    if (
        os.path.exists(INDEX_FILE)
        and os.path.exists(EMBED_FILE)
        and os.path.exists(DOC_FILE)
        and os.path.exists(FILEMAP_FILE)
    ):
        print("✅ Loading cached FAISS index and embeddings...")
        index = faiss.read_index(INDEX_FILE)
        with open(EMBED_FILE, "rb") as f:
            _ = pickle.load(f)  # Optional
        with open(DOC_FILE, "rb") as f:
            docs = pickle.load(f)
        with open(FILEMAP_FILE, "rb") as f:
            filenames = pickle.load(f)
        return index, docs, filenames

    print("🛠 Building index from scratch...")
    docs = []
    vectors = []
    filenames = []

    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                content = f.read()
                docs.append(content)
                filenames.append(fname)
                emb = get_titan_embedding(content[:1000])
                vectors.append(emb.astype("float32"))

    embeddings = np.array(vectors)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save all 3 things
    faiss.write_index(index, INDEX_FILE)
    with open(EMBED_FILE, "wb") as f:
        pickle.dump(embeddings, f)
    with open(DOC_FILE, "wb") as f:
        pickle.dump(docs, f)
    with open(FILEMAP_FILE, "wb") as f:
        pickle.dump(filenames, f)

    return index, docs, filenames
