import os
from langchain_chroma import Chroma
from multiweb_assistant.config import (VECTOR_STORE_PATH,TOP_K_RESULTS,)
from multiweb_assistant.embedding import get_embedding_model

# --------------------------------------------------
# Build Vector Store
# --------------------------------------------------
def build_vector_store(chunks):
    """Build and persist a Chroma vector store from chunks."""
    try:
        embedding_model = get_embedding_model()
        if embedding_model is None:
            print("Error: Embedding model could not be loaded.")
            return None
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=VECTOR_STORE_PATH,
        )
        return vector_store
    except Exception as e:
        print(f"Error building vector store: {e}")
        return None

# --------------------------------------------------
# Save Vector Store
# --------------------------------------------------
def save_vector_store(vector_store,path: str = VECTOR_STORE_PATH) -> None:
    """
    Ensure the Chroma vector store directory exists.
    Chroma automatically persists data when
    persist_directory is configured.
    """
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Error saving vector store: {e}")

# --------------------------------------------------
# Check Vector Store
# --------------------------------------------------
def vector_store_exists(path: str = VECTOR_STORE_PATH) -> bool:
    """Check whether a persisted Chroma database exists."""
    try:
        if not os.path.exists(path):
            return False
        return any(os.scandir(path))
    except Exception as e:
        print(f"Error checking vector store: {e}")
        return False
    
# --------------------------------------------------
# Load Vector Store
# --------------------------------------------------
def load_vector_store(path: str = VECTOR_STORE_PATH):
    """Load an existing Chroma vector store."""
    try:
        embedding_model = get_embedding_model()
        if embedding_model is None:
            print("Error: Embedding model could not be loaded.")
            return None
        vector_db = Chroma(
            persist_directory=path,
            embedding_function=embedding_model,
        )
        return vector_db
    except Exception as e:
        print(f"Error loading vector store: {e}")
        return None

# --------------------------------------------------
# Retriever
# --------------------------------------------------

def get_retriever(vector_store,k: int = TOP_K_RESULTS):
    """Return a retriever that returns top-k chunks."""
    try:
        return vector_store.as_retriever(
            search_kwargs={
                "k": k
            }
        )
    except Exception as e:
        print(f"Error creating retriever: {e}")
        return None