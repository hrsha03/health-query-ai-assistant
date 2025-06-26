from core.embedder import get_titan_embedding
import numpy as np

def retrieve(query, index, docs, filenames, top_k=1):
    from core.embedder import get_titan_embedding
    import numpy as np

    q_vec = get_titan_embedding(query).astype("float32").reshape(1, -1)
    distances, indices = index.search(q_vec, top_k)
    return [(docs[i], filenames[i]) for i in indices[0]]
