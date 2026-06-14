# from collections import defaultdict


# class HybridRetriever:

#     def __init__(self, vector_retriever, bm25_retriever):
#         self.vector_retriever = vector_retriever
#         self.bm25_retriever = bm25_retriever

#     def retrieve(self, query, k=5):

#         vector_results = self.vector_retriever(query)

#         bm25_results = self.bm25_retriever.retrieve(query, k)

#         scores = defaultdict(float)

#         chunk_lookup = {}

#         # BM25 results contain full Document objects
#         for i, (chunk, _) in enumerate(bm25_results):

#             text = chunk.page_content

#             scores[text] += (k - i)

#             chunk_lookup[text] = chunk

#         # Vector results contain only text
#         for i, doc_text in enumerate(
#             vector_results["documents"][0]
#         ):

#             scores[doc_text] += (k - i)

#         ranked = sorted(
#             scores.items(),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         results = []

#         for text, score in ranked[:k]:

#             if text in chunk_lookup:

#                 results.append(
#                     (chunk_lookup[text], score)
#                 )

#         return results


# from collections import defaultdict


# class HybridRetriever:

#     def __init__(
#         self,
#         vector_retriever,
#         bm25_retriever
#     ):
#         self.vector_retriever = vector_retriever
#         self.bm25_retriever = bm25_retriever

#     def retrieve(self, query, k=5):

#         vector_results = self.vector_retriever(query)

#         bm25_results = self.bm25_retriever.retrieve(
#             query,
#             k
#         )

#         scores = defaultdict(float)

#         # -------------------------
#         # Vector Search Results
#         # -------------------------

#         for i, doc in enumerate(
#             vector_results["documents"][0]
#         ):

#             scores[doc] += (k - i)

#         # -------------------------
#         # BM25 Results
#         # -------------------------

#         for i, (chunk, _) in enumerate(
#             bm25_results
#         ):

#             scores[
#                 chunk.page_content
#             ] += (k - i)

#         ranked = sorted(
#             scores.items(),
#             key=lambda x: x[1],
#             reverse=True
#         )

#         final_results = []

#         for text, score in ranked[:k]:

#             page = None
#             chunk_id = None

#             for chunk, _ in bm25_results:

#                 if chunk.page_content == text:

#                     page = chunk.metadata.get(
#                         "page"
#                     )

#                     chunk_id = chunk.metadata.get(
#                         "chunk_id"
#                     )

#                     break

#             final_results.append(
#                 (
#                     {
#                         "text": text,
#                         "page": page,

#                         "chunk_id": chunk_id
#                     },
#                     score
#                 )
#             )

#         return final_results




from collections import defaultdict


class HybridRetriever:

    def __init__(
        self,
        vector_retriever,
        bm25_retriever
    ):
        self.vector_retriever = vector_retriever
        self.bm25_retriever = bm25_retriever

    def retrieve(self, query, k=5):

        vector_results = self.vector_retriever(query)

        bm25_results = self.bm25_retriever.retrieve(
            query,
            k
        )

        scores = defaultdict(float)

        docs_map = {}

        # -------------------------
        # Vector Results
        # -------------------------

        for i, doc_text in enumerate(
            vector_results["documents"][0]
        ):

            scores[doc_text] += (k - i)

            if doc_text not in docs_map:

                docs_map[doc_text] = {
                    "text": doc_text,
                    "metadata": {}
                }

        # -------------------------
        # BM25 Results
        # -------------------------

        for i, (chunk, bm25_score) in enumerate(
            bm25_results
        ):

            text = chunk.page_content

            scores[text] += (k - i)

            docs_map[text] = {
                "text": text,
                "metadata": chunk.metadata
            }

        # -------------------------
        # Final Ranking
        # -------------------------

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        final_results = []

        for text, score in ranked[:k]:

            doc = docs_map[text]

            doc["hybrid_score"] = float(score)

            final_results.append(doc)

        return final_results

        print("\nDEBUG HYBRID RESULTS")

        for doc in final_results:

            print(
            doc["metadata"]
            ) 