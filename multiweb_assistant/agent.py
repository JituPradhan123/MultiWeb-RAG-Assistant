from langchain.agents import create_agent
from multiweb_assistant.config import SYSTEM_PROMPT

def create_multiweb_agent(llm, tools):
    """Return a LangChain agent that can call our tools and answer the questions."""
    try:
        chat_agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=SYSTEM_PROMPT
        )
        return chat_agent
    except Exception as e:
        print(f"Error creating multiweb agent: {e}")
        return None