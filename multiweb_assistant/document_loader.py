from multiweb_assistant.webpageloader import WebPageLoader
from multiweb_assistant.config import urls

def load_documents(urls: str = urls):
    """Load data from URLs and return it as a list of LangChain Documents."""
    try:
        loader = WebPageLoader(urls)
        documents = loader.load()
        return documents
    except Exception as e:
        print(f"Error loading documents: {e}")
        return []
