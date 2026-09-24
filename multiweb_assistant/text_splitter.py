from langchain_text_splitters import RecursiveCharacterTextSplitter
from multiweb_assistant.config import CHUNK_OVERLAP, CHUNK_SIZE

def split_to_chunks(documents):
    """Split the documents into chunks."""
    try:
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = text_spliter.split_documents(documents)
        return chunks
    except Exception as e:
        print(f"Error splitting documents into chunks: {e}")
        return []