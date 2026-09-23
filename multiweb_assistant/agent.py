from langchain.agents import create_agent
from multiweb_assistant.config import SYSTEM_PROMPT

def create_multiweb_agent(llm,tools):
        """ Return a LangChain agent that can call our tools and answer the questions """
        chat_agent = create_agent(
            model = llm,
            tools = tools,
            system_prompt= SYSTEM_PROMPT
        )
        return chat_agent
    