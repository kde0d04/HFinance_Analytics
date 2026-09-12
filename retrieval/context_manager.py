from retrieval.retriever import get_retriever, retrieve_context
from retrieval.query_parser import parse_query

def get_context(user_input):
    """Combine query parsing + retrieval"""
    parsed = parse_query(user_input)
    retriever = get_retriever()
    context = retrieve_context(parsed["original"], retriever)
    return context
