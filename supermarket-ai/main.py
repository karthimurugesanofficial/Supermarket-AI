from utils import load_product_data, row_to_text
from embeddings import get_embeddings
from vectordb import VectorStore
from prompt_builder import build_prompt
from llm_interface import query_deepseek
from sentence_transformers import SentenceTransformer

def main(user_query):
    # Load CSV
    df = load_product_data()
    texts = df.apply(row_to_text, axis=1).tolist()

    # Create embeddings
    embeddings = get_embeddings(texts)

    # Initialize FAISS
    vector_store = VectorStore(dim=embeddings[0].shape[0])
    vector_store.add_embeddings(embeddings, texts)

    # Embed the query
    query_embedding = get_embeddings([user_query])

    # Search top-k
    relevant_chunks = vector_store.query(query_embedding)

    # Build prompt and query LLM
    prompt = build_prompt(relevant_chunks, user_query)
    reply = query_deepseek(prompt)
    
    return reply


# 🔍 Run this test
if __name__ == "__main__":
    user_input = "Is detergent available?"
    response = main(user_input)
    print("💬 Bot:", response)
