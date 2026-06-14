# from app.injestion.loader import load_pdf
# from app.injestion.clean import clean_documents
# from app.injestion.chunker import split_documents
# from app.injestion.embeddings import generate_embeddings
# from app.retrieval.vector_store import store_chunks
# from app.retrieval.retriever import retrieve
# from app.retrieval.bm25_retriever import BM25Retriever

# def main():

#     print("\n" + "=" * 60)
#     print("STEP 1 : LOADING PDF")
#     print("=" * 60)

#     docs = load_pdf("data/summer_internship.pdf")

#     print(f"\nDocuments Loaded: {len(docs)}")

#     if not docs:
#         print("No documents loaded!")
#         return

#     print("\nFirst Document Metadata:")
#     print(docs[0].metadata)

#     print("\nFirst Document Length:")
#     print(len(docs[0].page_content), "characters")

#     print("\nFirst Document Preview (RAW):")
#     print("-" * 60)
#     print(docs[0].page_content[:500])
#     print("-" * 60)

#     print("\n" + "=" * 60)
#     print("STEP 2 : CLEANING TEXT")
#     print("=" * 60)

#     cleaned_docs = clean_documents(docs)

#     print("\nFirst Document Preview (CLEANED):")
#     print("-" * 60)
#     print(cleaned_docs[0].page_content[:500])
#     print("-" * 60)

#     print("\n" + "=" * 60)
#     print("STEP 3 : CHUNKING")
#     print("=" * 60)

#     chunks = split_documents(cleaned_docs)

#     print(f"\nChunks Created: {len(chunks)}")

#     if not chunks:
#         print("No chunks created!")
#         return

#     print("\nFirst Chunk Metadata:")
#     print(chunks[0].metadata)

#     print("\nFirst Chunk Length:")
#     print(len(chunks[0].page_content), "characters")

#     print("\nFirst Chunk Preview:")
#     print("-" * 60)
#     print(chunks[0].page_content[:500])
#     print("-" * 60)

#     print("\n" + "=" * 60)
#     print("CHUNK SUMMARY")
#     print("=" * 60)

#     for i, chunk in enumerate(chunks):

#         print(f"\nChunk {i+1}")
#         print(f"Page       : {chunk.metadata.get('page')}")
#         print(f"Length     : {len(chunk.page_content)}")
#         print(
#             f"Start Index: {chunk.metadata.get('start_index', 'N/A')}"
#         )
#         print(
#             f"Chunk ID   : {chunk.metadata.get('chunk_id', 'Not Added Yet')}"
#         )

#     print("\n" + "=" * 60)
#     print("CHUNK PREVIEWS")
#     print("=" * 60)

#     for i, chunk in enumerate(chunks):

#         print(f"\n----- Chunk {i+1} -----")
#         print(chunk.page_content[:200])

#     print("\n" + "=" * 60)
#     print("PIPELINE SUCCESS")
#     print("=" * 60)

#     print("\n" + "=" * 60)
#     print("STEP 4 : EMBEDDINGS")
#     print("=" * 60)

#     embeddings = generate_embeddings(chunks)

#     print(f"\nEmbeddings Generated: {len(embeddings)}")

#     print("\nEmbedding Dimension:")
#     print(len(embeddings[0]))

#     print("\nFirst 10 Values:")
#     print(embeddings[0][:10])

#     store_chunks(chunks, embeddings)
#     print("\nStored in ChromaDB")
    
#     query = "What are the internship deliverables?"

#     results = retrieve(query)

#     print("\nRETRIEVED CHUNKS\n")

#     for doc in results["documents"][0]:
#       print("=" * 50)
#       print(doc[:500])
      
# if __name__ == "__main__":
#     main()


# from app.retrieval.retriever import retrieve
# from app.retrieval.bm25_retriever import BM25Retriever

# from app.injestion.loader import load_pdf
# from app.injestion.clean import clean_documents
# from app.injestion.chunker import split_documents

# from app.retrieval.hybrid_retrieval import HybridRetriever
# from app.retrieval.reranker import Reranker

# def main():

#     query = "What are the internship deliverables?"

#     print("\n")
#     print("=" * 60)
#     print("VECTOR RETRIEVAL")
#     print("=" * 60)

#     vector_results = retrieve(query)

#     for doc in vector_results["documents"][0]:

#         print("\n")
#         print("-" * 50)
#         print(doc[:400])

#     # BM25 needs chunks

#     docs = load_pdf("data/summer_internship.pdf")

#     docs = clean_documents(docs)

#     chunks = split_documents(docs)

#     bm25 = BM25Retriever(chunks)

#     print("\n")
#     print("=" * 60)
#     print("BM25 RETRIEVAL")
#     print("=" * 60)

#     bm25_results = bm25.retrieve(query)

#     for chunk, score in bm25_results:

#         print("\n")
#         print(f"Score : {score:.4f}")
#         print("-" * 50)
#         print(chunk.page_content[:400])

#     print("\n")
#     print("=" * 60)
#     print("HYBRID RETRIEVAL")
#     print("=" * 60)

#     hybrid = HybridRetriever(
#         retrieve,
#         bm25
#     )

#     hybrid_results = hybrid.retrieve(query)

    
#     for doc, score in hybrid_results:

#         print("\n")
#         print(f"Combined Score : {score}")
#         print("-" * 50)
#         print(doc[:400])
    
#     # Prepare docs for reranker
#     hybrid_docs = [
#     doc
#     for doc, score in hybrid_results
#     ]
    
#     print("\n")
#     print("=" * 60)
#     print("CROSS ENCODER RERANKING")
#     print("=" * 60)

#     reranker = Reranker()

#     reranked = reranker.rerank(
#        query,
#        hybrid_docs,
#        top_k=3
#      )

#     for doc, score in reranked:

#       print("\n")
#       print(f"Reranker Score : {score:.4f}")
#       print("-" * 50)
#       print(doc[:400])


# if __name__ == "__main__":
#     main()


# from app.retrieval.retriever import retrieve
# from app.retrieval.bm25_retriever import BM25Retriever
# from app.retrieval.hybrid_retrieval import HybridRetriever
# from app.retrieval.reranker import Reranker

# from app.injestion.loader import load_pdf
# from app.injestion.clean import clean_documents
# from app.injestion.chunker import split_documents
# from app.generation.prompt_builder import build_prompt
# from app.generation.generator import generate_answer

# def main():

#     query = "Is the internship remote?"

#     # ==================================================
#     # LOAD + PREPROCESS
#     # ==================================================

#     docs = load_pdf("data/summer_internship.pdf")

#     docs = clean_documents(docs)

#     chunks = split_documents(docs)

#     # ==================================================
#     # VECTOR RETRIEVAL
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("VECTOR RETRIEVAL")
#     print("=" * 60)

#     vector_results = retrieve(query)

#     for doc in vector_results["documents"][0]:

#         print("\n")
#         print("-" * 50)
#         print(doc[:400])

#     # ==================================================
#     # BM25 RETRIEVAL
#     # ==================================================

#     bm25 = BM25Retriever(chunks)

#     print("\n")
#     print("=" * 60)
#     print("BM25 RETRIEVAL")
#     print("=" * 60)

#     bm25_results = bm25.retrieve(query)

#     for chunk, score in bm25_results:

#      print("\n")
#      print(f"BM25 Score : {score:.4f}")
#      print("-" * 50)
#      print(chunk.page_content[:400])

#     # ==================================================
#     # HYBRID RETRIEVAL
#     # ==================================================

#     hybrid = HybridRetriever(
#         retrieve,
#         bm25
#     )

#     print("\n")
#     print("=" * 60)
#     print("HYBRID RETRIEVAL")
#     print("=" * 60)

#     hybrid_results = hybrid.retrieve(query)

#     for doc, score in hybrid_results:

#         print("\n")
#         print(f"Combined Score : {score:.4f}")
#         print("-" * 50)
#         print(doc[:400])

#     # ==================================================
#     # PREPARE DOCS FOR RERANKER
#     # ==================================================

#     hybrid_docs = [
#         doc
#         for doc, score in hybrid_results
#     ]

#     # ==================================================
#     # CROSS ENCODER RERANKING
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("CROSS ENCODER RERANKING")
#     print("=" * 60)

#     reranker = Reranker()

#     reranked = reranker.rerank(
#         query,
#         hybrid_docs,
#         top_k=3
#     )

#     for rank, (doc, score) in enumerate(reranked, start=1):

#         print("\n")
#         print(f"Rank : {rank}")
#         print(f"Reranker Score : {score:.4f}")
#         print("-" * 50)
#         print(doc[:400])
    

#     contexts = [
#     doc
#     for doc, score in reranked
#     ]

#     prompt = build_prompt(
#     query,
#     contexts
#     )

#     answer = generate_answer(
#     prompt
#     )


#     print("\n")
#     print("=" * 60)
#     print("PIPELINE COMPLETE")
#     print("=" * 60)
    
#     print("\n")
#     print("=" * 60)
#     print("FINAL ANSWER")
#     print("=" * 60)

#     print(answer)

# if __name__ == "__main__":
#     main()

# from app.retrieval.retriever import retrieve
# from app.retrieval.bm25_retriever import BM25Retriever
# from app.retrieval.hybrid_retrieval import HybridRetriever
# from app.retrieval.reranker import Reranker

# from app.injestion.loader import load_pdf
# from app.injestion.clean import clean_documents
# from app.injestion.chunker import split_documents

# from app.generation.prompt_builder import build_prompt
# from app.generation.generator import generate_answer


# def main():

#     query = "What is the internship duration?"

#     # ==================================================
#     # LOAD + CLEAN + CHUNK
#     # ==================================================

#     docs = load_pdf("data/summer_internship.pdf")

#     docs = clean_documents(docs)

#     chunks = split_documents(docs)

#     # ==================================================
#     # VECTOR RETRIEVAL
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("VECTOR RETRIEVAL")
#     print("=" * 60)

#     vector_results = retrieve(query)

#     for doc in vector_results["documents"][0]:

#         print("\n")
#         print("-" * 50)
#         print(doc[:400])

#     # ==================================================
#     # BM25 RETRIEVAL
#     # ==================================================

#     bm25 = BM25Retriever(chunks)

#     print("\n")
#     print("=" * 60)
#     print("BM25 RETRIEVAL")
#     print("=" * 60)

#     bm25_results = bm25.retrieve(query)

#     for chunk, score in bm25_results:

#         print("\n")
#         print(f"BM25 Score : {score:.4f}")
#         print("-" * 50)
#         print(chunk.page_content[:400])

#     # ==================================================
#     # HYBRID RETRIEVAL
#     # ==================================================

#     hybrid = HybridRetriever(
#         retrieve,
#         bm25
#     )

#     print("\n")
#     print("=" * 60)
#     print("HYBRID RETRIEVAL")
#     print("=" * 60)

#     hybrid_results = hybrid.retrieve(query)

#     for item, score in hybrid_results:

#         print("\n")
#         print(f"Combined Score : {score:.4f}")
#         print("-" * 50)
#         print(item["text"][:400])

#     # ==================================================
#     # CROSS ENCODER RERANKING
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("CROSS ENCODER RERANKING")
#     print("=" * 60)

#     reranker = Reranker()

#     reranked = reranker.rerank(
#         query,
#         [item for item, score in hybrid_results],
#         top_k=3
#     )

#     for rank, (doc, score) in enumerate(reranked, start=1):

#         print("\n")
#         print(f"Rank : {rank}")
#         print(f"Reranker Score : {score:.4f}")
#         print(f"Page : {doc['page']}")
#         print("-" * 50)
#         print(doc["text"][:400])

#     # ==================================================
#     # PROMPT BUILDING
#     # ==================================================

#     contexts = []

#     for doc, score in reranked:

#         context = f"""
# [Page {doc['page']}]

# {doc['text']}
# """

#         contexts.append(context)

#     prompt = build_prompt(
#         query,
#         contexts
#     )

#     # ==================================================
#     # GENERATION
#     # ==================================================

#     answer = generate_answer(prompt)

#     # ==================================================
#     # FINAL OUTPUT
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("FINAL ANSWER")
#     print("=" * 60)

#     print(answer)

#     # ==================================================
#     # CITATIONS
#     # ==================================================

#     print("\n")
#     print("=" * 60)
#     print("SOURCES")
#     print("=" * 60)

#     for i, (doc, score) in enumerate(reranked, start=1):

#         print(
#             f"[{i}] Page {doc['page']} | Chunk ID: {doc['chunk_id']}"
#         )

#     print("\n")
#     print("=" * 60)
#     print("PIPELINE COMPLETE")
#     print("=" * 60)


# if __name__ == "__main__":
#     main()






from app.retrieval.retriever import retrieve
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.hybrid_retrieval import HybridRetriever
from app.retrieval.reranker import Reranker

from app.injestion.loader import load_pdf
from app.injestion.clean import clean_documents
from app.injestion.chunker import split_documents

from app.generation.prompt_builder import build_prompt
from app.generation.generator import generate_answer


def main():

    query = "What is the internship duration?"

    # ==================================================
    # LOAD + CLEAN + CHUNK
    # ==================================================

    docs = load_pdf("data/summer_internship.pdf")
    docs = clean_documents(docs)
    chunks = split_documents(docs)

    # ==================================================
    # VECTOR RETRIEVAL
    # ==================================================

    print("\n")
    print("=" * 60)
    print("VECTOR RETRIEVAL")
    print("=" * 60)

    vector_results = retrieve(query)

    for doc in vector_results["documents"][0]:

        print("\n")
        print("-" * 50)
        print(doc[:400])

    # ==================================================
    # BM25 RETRIEVAL
    # ==================================================

    bm25 = BM25Retriever(chunks)

    print("\n")
    print("=" * 60)
    print("BM25 RETRIEVAL")
    print("=" * 60)

    bm25_results = bm25.retrieve(query)

    for chunk, score in bm25_results:

        print("\n")
        print(f"BM25 Score : {score:.4f}")
        print("-" * 50)
        print(chunk.page_content[:400])

    # ==================================================
    # HYBRID RETRIEVAL
    # ==================================================

    hybrid = HybridRetriever(
        retrieve,
        bm25
    )

    print("\n")
    print("=" * 60)
    print("HYBRID RETRIEVAL")
    print("=" * 60)

    hybrid_results = hybrid.retrieve(query)

    for doc in hybrid_results:

        print("\n")
        print(f"Combined Score : {doc['hybrid_score']:.4f}")
        print("-" * 50)
        print(doc["text"][:400])

    # ==================================================
    # CROSS ENCODER RERANKING
    # ==================================================

    print("\n")
    print("=" * 60)
    print("CROSS ENCODER RERANKING")
    print("=" * 60)

    reranker = Reranker()

    reranked = reranker.rerank(
        query,
        hybrid_results,
        top_k=3
    )

    for rank, doc in enumerate(reranked, start=1):

        print("\n")
        print(f"Rank : {rank}")
        print(f"Reranker Score : {doc['rerank_score']:.4f}")
        print(
            f"Page : {doc['metadata'].get('page')}"
        )

        print("-" * 50)
        print(doc["text"][:400])

    # ==================================================
    # PROMPT BUILDING
    # ==================================================

    contexts = []

    for doc in reranked:

        context = f"""
[Page {doc['metadata'].get('page')}]

{doc['text']}
"""

        contexts.append(context)

    prompt = build_prompt(
        query,
        contexts
    )

    # ==================================================
    # GENERATION
    # ==================================================

    answer = generate_answer(prompt)

    # ==================================================
    # FINAL ANSWER
    # ==================================================

    print("\n")
    print("=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)

    print(answer)

    # ==================================================
    # CITATIONS
    # ==================================================

    print("\n")
    print("=" * 60)
    print("SOURCES")
    print("=" * 60)

    for i, doc in enumerate(reranked, start=1):

        print(
            f"[{i}] "
            f"Page {doc['metadata'].get('page')} | "
            f"Chunk ID: {doc['metadata'].get('chunk_id')}"
        )

    print("\n")
    print("=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()