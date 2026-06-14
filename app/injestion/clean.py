import re
from langchain_core.documents import Document


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r" +", " ", text)

    return text.strip()


def clean_documents(documents):
    cleaned_docs = []

    for doc in documents:
        cleaned_doc = Document(
            page_content=clean_text(doc.page_content),
            metadata=doc.metadata
        )

        cleaned_docs.append(cleaned_doc)

    return cleaned_docs