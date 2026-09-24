from langchain_huggingface import HuggingFaceEmbeddings
from multiweb_assistant.config import EMBEDDING_MODEL_NAME, hf_token

def get_embedding_model():
    """Return embedding model from Hugging Face."""
    try:
        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={
                "token": hf_token
            }
        )
        return embedding_model
    except Exception as e:
        print(f"Error loading embedding model: {e}")
        return None

