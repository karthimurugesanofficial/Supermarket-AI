from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def get_embeddings(texts):
    return model.encode(texts)

