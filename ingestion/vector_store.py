from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def build_vector_store(docs, persist_directory="./vector_store"):
    """Create embeddings and store documents in ChromaDB"""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    return vectordb
