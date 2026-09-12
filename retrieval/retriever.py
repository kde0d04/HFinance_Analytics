from langchain_community.vectorstores import Chroma

def get_retriever(persist_directory="./vector_store"):
    """Load ChromaDB retriever"""
    vectordb = Chroma(persist_directory=persist_directory)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return retriever

def retrieve_context(query, retriever):
    """Retrieve relevant context for a query"""
    # Old: results = retriever.get_relevant_documents(query)
    results = retriever.invoke(query)   # ✅ Correct method
    return results
