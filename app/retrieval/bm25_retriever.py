from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, chunks):

        self.chunks = chunks

        corpus = [
            chunk.page_content.split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(corpus)

    def retrieve(self, query, k=3):

      tokenized_query = query.split()

      scores = self.bm25.get_scores(
        tokenized_query
      )

      ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
      )[:k]

      results = [
        (self.chunks[i], scores[i])
        for i in ranked_indices
      ]

      return results