"""Write all the components together into one ready-to-use agent.
This is the single entry point that main.py and app.py both call.
Each step is handled by its own small module.
"""

from multiweb_assistant import config
from multiweb_assistant.config import urls
from multiweb_assistant.vector_store import *
from multiweb_assistant.document_loader import load_documents
from multiweb_assistant.text_splitter import split_to_chunks
from multiweb_assistant.tools import create_search_tool
from multiweb_assistant.llm import get_llm
from multiweb_assistant.agent import create_multiweb_agent


def build_vector_database_for_document():
    """Load + split + embed the document, reusing a saved one if we have one."""

    try:
        if vector_store_exists():
            print("Found a saved vector store on disk")

            vector_store = load_vector_store()

            if vector_store is None:
                print("Error: Could not load the saved vector store.")
                return None

            return vector_store

        else:
            print("No saved vector database found")

            documents = load_documents()

            if not documents:
                print("Error: No documents were loaded.")
                return None

            chunks = split_to_chunks(documents)

            if not chunks:
                print("Error: No chunks were created.")
                return None

            print(f"Load and split it into {len(chunks)} chunks.")

            vector_store = build_vector_store(chunks)

            if vector_store is None:
                print("Error: Could not build the vector store.")
                return None

            save_vector_store(vector_store)

            print("Vector store build and saved to disk for next time.")

            return vector_store

    except Exception as e:
        print(f"Error building vector database: {e}")
        return None


def build_multiweb_assistant():
    """Build the full RAG agent, ready to answer questions."""

    try:
        config.check_api_keys()

        vector_store = build_vector_database_for_document()

        if vector_store is None:
            print("Error: Vector store is not available.")
            return None

        retriever = get_retriever(vector_store)

        if retriever is None:
            print("Error: Could not create retriever.")
            return None

        search_tool = create_search_tool(retriever)

        if search_tool is None:
            print("Error: Could not create search tool.")
            return None

        llm = get_llm()

        if llm is None:
            print("Error: Could not load LLM.")
            return None

        agent = create_multiweb_agent(
            llm,
            [search_tool]
        )

        if agent is None:
            print("Error: Could not create multiweb agent.")
            return None

        return agent

    except Exception as e:
        print(f"Error building multiweb assistant: {e}")
        return None


def ask(agent, question: str) -> str:
    """Ask the agent a question and return the final answer."""

    try:
        if agent is None:
            return "Error: Assistant is not available."

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        return response["messages"][-1].content

    except Exception as e:
        print(f"Error while asking the assistant: {e}")
        return "Sorry, an error occurred while processing your question."