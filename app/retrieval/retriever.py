from sentence_transformers import SentenceTransformer
from app.retrieval.vector_store import collection

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def retrieve(query, k=3):

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results