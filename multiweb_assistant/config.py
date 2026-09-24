""" All settings for the app live here, in one place."""

from dotenv import load_dotenv
import os
load_dotenv()

# Huggingface token

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Data Source
## Remove all the bellow Urls and add your urls in the bellow list
urls = [
    "https://jitupradhan.pythonanywhere.com/",
    "https://jitupradhan.pythonanywhere.com/domain/1/",
    "https://jitupradhan.pythonanywhere.com/domain/2/",
    "https://jitupradhan.pythonanywhere.com/domain/3/",
    "https://jitupradhan.pythonanywhere.com/media/resume/Master_Resume_1.pdf",
    "https://jitupradhan.pythonanywhere.com/media/certificates/Introduction_to_Data_Science_by_Infosis.pdf",
    "https://jitupradhan.pythonanywhere.com/media/certificates/certificate_data_analyst.pdf",
    "https://jitupradhan.pythonanywhere.com/media/certificates/Brainware_University_Jitu_Pradhan_Intel_Unnati_1.pdf",
    "https://jitupradhan.pythonanywhere.com/media/certificates/Data_Analyst_Job_Semulation_by_Deloitte.pdf"      
]

# Vector store

VECTOR_STORE_PATH = os.path.join("vector_data","chroma")

# Embedding model

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# llm model

LLM_MODEL_NAME = "zai-org/GLM-5.3"
LLM_MODEL_TEMPERATURE = 0
LLM_TASK = "text-generation"
LLM_MAX_NEW_TOKEN = 500


## Chunk / Text Splitting Config

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


# Retrival Results

TOP_K_RESULTS = 3

# System Instructions

SYSTEM_PROMPT=(
    "You are a friendly assistant for website."
    "Always use the search_details tool to look up"
    "fatch before answering."
    "If the answer is not in the search results, say you don't know"
    "instead of guessing."
)

def check_api_keys() -> None:
    """ Stop early with a clear message if a required API key is missing"""
    if not hf_token:
        raise ValueError("Missing Huggingface API. Add it to your codebase")