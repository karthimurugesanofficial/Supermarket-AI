from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from embeddings import get_embeddings


def search_top_k(query, df, k=3):
    # Get texts from DataFrame
    texts = df.apply(lambda row: f"{row['product_name']} - {row['brand']} - {row['category']} - ₹{row['price']}", axis=1).tolist()

    # Encode with shared embedding model
    corpus_embeddings = get_embeddings(texts)
    query_embedding = get_embeddings([query])

    # Normalize (optional but recommended)
    faiss.normalize_L2(corpus_embeddings)
    faiss.normalize_L2(query_embedding)

    # Build FAISS index and search
    index = faiss.IndexFlatL2(corpus_embeddings[0].shape[0])
    index.add(np.array(corpus_embeddings))
    distances, indices = index.search(np.array(query_embedding), k)

    # Return top k results
    return "\n".join([texts[i] for i in indices[0]])
