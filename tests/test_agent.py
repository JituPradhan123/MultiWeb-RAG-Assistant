from multiweb_assistant.agent import create_multiweb_agent
from multiweb_assistant.llm import get_llm
from multiweb_assistant.tools import create_search_tool


class FakeRetriever:
    """Simple retriever for testing the agent tool."""

    def invoke(self, question):

        from langchain_core.documents import Document

        return [
            Document(
                page_content=(
                    "Jitu Pradhan is experienced in Python, "
                    "Django, Machine Learning and SQL."
                ),
                metadata={
                    "source": "test_resume"
                },
            )
        ]


def test_create_multiweb_agent():

    # --------------------------------------------------
    # 1. Create LLM
    # --------------------------------------------------

    llm = get_llm()

    assert llm is not None

    print("\n✅ LLM created")

    # --------------------------------------------------
    # 2. Create retriever
    # --------------------------------------------------

    retriever = FakeRetriever()

    # --------------------------------------------------
    # 3. Create search tool
    # --------------------------------------------------

    search_tool = create_search_tool(retriever)

    assert search_tool is not None

    print("✅ Search tool created")

    # --------------------------------------------------
    # 4. Create agent
    # --------------------------------------------------

    agent = create_multiweb_agent(
        llm=llm,
        tools=[search_tool],
    )

    assert agent is not None

    print("✅ Agent created successfully")

    # --------------------------------------------------
    # 5. Test agent
    # --------------------------------------------------

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What skills does Jitu have?"
                }
            ]
        }
    )

    # --------------------------------------------------
    # 6. Check response
    # --------------------------------------------------

    assert response is not None
    assert "messages" in response

    messages = response["messages"]

    assert messages

    final_message = messages[-1]

    print("\nAgent response:")
    print(final_message.content)

    assert final_message.content

    print("\n" + "=" * 70)
    print("✅ AGENT TEST PASSED")
    print("=" * 70)