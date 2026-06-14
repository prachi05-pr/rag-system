# from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader


# loader = OpenDataLoaderPDFLoader(
#     file_path= "data/summer_internship.pdf",
#     format="text"
#   )
# documents = loader.load()

# for doc in documents:
#     print(doc.metadata, doc.page_content[:5000])
 
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents
