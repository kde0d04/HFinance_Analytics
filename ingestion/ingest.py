import pandas as pd
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, CSVLoader

def load_data(file_path):
    """Load data from CSV, Excel, PDF, DOCX"""
    if file_path.endswith(".csv"):
        loader = CSVLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
        docs = loader.load()
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        docs = [df.to_string()]
    else:
        raise ValueError("Unsupported file format")
    return docs
