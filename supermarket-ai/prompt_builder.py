def build_prompt(context_chunks, user_query):
    context = "\n".join(context_chunks)
    return f"""You are an AI supermarket assistant. Use the data below to answer the user.

Product Information:
{context}

User Query: {user_query}
Answer:"""
