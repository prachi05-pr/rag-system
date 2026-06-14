# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,  # chunk size (characters)
#     chunk_overlap=200,  # chunk overlap (characters)
#     add_start_index=True,  # track index in original document
# )
# all_splits = text_splitter.split_documents(data/hs.pdf)

# print(f"Split blog post into {len(all_splits)} sub-documents.")

# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def split_documents(docs):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200,
#         add_start_index=True
#     )

#     splits = text_splitter.split_documents(docs)

#     return splits


import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(docs)

    for chunk in chunks:
        chunk.metadata["chunk_id"] = str(uuid.uuid4())

    return chunks