from langchain_text_splitters import RecursiveCharacterTextSplitter
from multiweb_assistant.config import CHUNK_OVERLAP, CHUNK_SIZE

def split_to_chunks(documents):
    """Split the ducuments in to chunks"""
    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )
    chunks = text_spliter.split_documents(documents)
    return chunks