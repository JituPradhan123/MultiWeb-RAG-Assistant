""" Connect the llm to the brain of the brain of the assistant """

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from multiweb_assistant.config import LLM_MAX_NEW_TOKEN, LLM_MODEL_NAME, LLM_TASK,LLM_MODEL_TEMPERATURE

def get_llm():
    """Return llm chat model"""
    text_gen_llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL_NAME,
        max_new_tokens=LLM_MAX_NEW_TOKEN,
        task= LLM_TASK,
        temperature=LLM_MODEL_TEMPERATURE
    )
    llm = ChatHuggingFace(llm=text_gen_llm)
    return llm

    