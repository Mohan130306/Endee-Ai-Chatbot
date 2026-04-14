from embedder import get_embedding
from vector_store import search

def get_answer(query):
    query_embedding = get_embedding(query)
    results = search(query_embedding)

    context = " ".join([r["text"] for r in results])

    # simple mock response
    return f"Based on documents: {context}"