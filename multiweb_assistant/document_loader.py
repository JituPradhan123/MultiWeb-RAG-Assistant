from multiweb_assistant.webpageloader import WebPageLoader
from multiweb_assistant.config import urls

def load_documents(urls:str = urls):
    """Load a data from urls and return it as a list of Langchain Document"""
    loader = WebPageLoader(urls)
    documents = loader.load()
    return documents
