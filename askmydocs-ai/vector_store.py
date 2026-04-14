from sklearn.metrics.pairwise import cosine_similarity

database = []

def store_vector(text, embedding):
    database.append({
        "text": text,
        "embedding": embedding
    })

def search(query_embedding):
    if not database:
        return []

    similarities = []

    for item in database:
        score = cosine_similarity(
            [query_embedding],
            [item["embedding"]]
        )[0][0]

        similarities.append((score, item))

    # sort by best match
    similarities.sort(reverse=True, key=lambda x: x[0])

    # return top 2
    return [item for _, item in similarities[:2]]