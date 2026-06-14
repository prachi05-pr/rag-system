# from sentence_transformers import CrossEncoder


# class Reranker:

#     def __init__(self):

#         self.model = CrossEncoder(
#             "cross-encoder/ms-marco-MiniLM-L-6-v2"
#         )

#     def rerank(self, query, retrieved_chunks, top_k=3):

#         pairs = [
#             (query, chunk.page_content)
#             for chunk, _ in retrieved_chunks
#         ]

#         scores = self.model.predict(pairs)

#         ranked = sorted(
#             zip(retrieved_chunks, scores),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         return ranked[:top_k]


# from sentence_transformers import CrossEncoder


# class Reranker:

#     def __init__(self):

#         self.model = CrossEncoder(
#             "cross-encoder/ms-marco-MiniLM-L-6-v2"
#         )

#     def rerank(
#         self,
#         query,
#         retrieved_docs,
#         top_k=3
#     ):

#         pairs = [

#             (
#                 query,
#                 doc["text"]
#             )

#             for doc in retrieved_docs
#         ]

#         scores = self.model.predict(
#             pairs
#         )

#         ranked = sorted(
#             zip(
#                 retrieved_docs,
#                 scores
#             ),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         return ranked[:top_k]



from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query,
        retrieved_docs,
        top_k=3
    ):

        pairs = [

            (
                query,
                doc["text"]
            )

            for doc in retrieved_docs
        ]

        scores = self.model.predict(
            pairs
        )

        reranked_docs = []

        for doc, score in zip(
            retrieved_docs,
            scores
        ):

            doc["rerank_score"] = float(score)

            reranked_docs.append(doc)

        reranked_docs.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return reranked_docs[:top_k]