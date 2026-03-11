from langchain.document_loaders import PyPDFLoader

def load_docs(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
