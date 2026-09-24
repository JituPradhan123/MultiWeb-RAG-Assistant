"""Connect the LLM to the brain of the assistant."""
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from multiweb_assistant.config import (LLM_MAX_NEW_TOKEN,LLM_MODEL_NAME,LLM_TASK,LLM_MODEL_TEMPERATURE)

def get_llm():
    """Return LLM chat model."""
    try:
        text_gen_llm = HuggingFaceEndpoint(
            repo_id=LLM_MODEL_NAME,
            max_new_tokens=LLM_MAX_NEW_TOKEN,
            task=LLM_TASK,
            temperature=LLM_MODEL_TEMPERATURE
        )
        llm = ChatHuggingFace(
            llm=text_gen_llm
        )
        return llm
    except Exception as e:
        print(f"Error loading LLM: {e}")
        return None