""" Write al the componemt to geather into one ready-to-use agent.
This is the single entry point that main.py and app.py both call. 
each  step is handled by its own smal module"""

from multiweb_assistant import config
from multiweb_assistant.config import urls
from multiweb_assistant.vector_store import *
from multiweb_assistant.document_loader import load_documents
from multiweb_assistant.text_splitter import split_to_chunks
from multiweb_assistant.tools import create_search_tool
from multiweb_assistant.llm import get_llm
from multiweb_assistant.agent import create_multiweb_agent

def build_vector_database_for_document():
    """Load + split + embed the document, reusing a saved if we have one."""
    if vector_store_exists():
        print("Found a saved vector store on disk")
        return load_vector_store()
    else:
        print("No saved vector database found")
        documents = load_documents()
        chunks = split_to_chunks(documents)
        print(f"Load and split it into {len(chunks)} chunks.")
        vector_store = build_vector_store(chunks)
        save_vector_store(vector_store)
        print("Vector store build and saved to disk for next time.")
        return vector_store
        
        

def build_multiweb_assistant():
    """ Bulid the full RAG agent , ready to answer questions"""
    config.check_api_keys()
    vector_store = build_vector_database_for_document()
    retriever = get_retriever(vector_store)
    search_tool = create_search_tool(retriever)
    
    llm = get_llm()
    agent = create_multiweb_agent(llm,[search_tool])
    
    return agent   


def ask(agent, question:str)-> str:
    """ Ask the agent a question and return the final answer """
    
    response = agent.invoke({"messages":[{"role":"user","content":question}]})
    return response["messages"][-1].content