from langchain_core.documents import Document

from multiweb_assistant.tools import create_search_tool


class FakeRetriever:
    """Fake retriever used for testing."""

    def invoke(self, question):

        assert question == "Tell me about Jitu's Python skills."

        return [
            Document(
                page_content=(
                    "Jitu has experience with Python, "
                    "Django and Machine Learning."
                ),
                metadata={
                    "source": "test_resume"
                },
            ),
            Document(
                page_content=(
                    "He has also worked with SQL and Power BI."
                ),
                metadata={
                    "source": "test_resume"
                },
            ),
        ]


def test_create_search_tool():

    # --------------------------------------------------
    # 1. Create fake retriever
    # --------------------------------------------------

    retriever = FakeRetriever()

    # --------------------------------------------------
    # 2. Create search tool
    # --------------------------------------------------

    search_tool = create_search_tool(retriever)

    # --------------------------------------------------
    # 3. Check tool was created
    # --------------------------------------------------

    assert search_tool is not None

    print("\n✅ Search tool created successfully")

    # --------------------------------------------------
    # 4. Check tool name
    # --------------------------------------------------

    assert search_tool.name == "search_details"

    print(f"Tool name: {search_tool.name}")

    # --------------------------------------------------
    # 5. Check tool description
    # --------------------------------------------------

    assert search_tool.description

    print(f"Tool description: {search_tool.description}")

    # --------------------------------------------------
    # 6. Execute the tool
    # --------------------------------------------------

    question = "Tell me about Jitu's Python skills."

    result = search_tool.invoke(
        {
            "question": question
        }
    )

    # --------------------------------------------------
    # 7. Check result
    # --------------------------------------------------

    assert result
    assert isinstance(result, str)

    print("\nSearch result:")
    print(result)

    # --------------------------------------------------
    # 8. Verify retrieved information
    # --------------------------------------------------

    assert "Python" in result
    assert "Django" in result
    assert "Machine Learning" in result
    assert "SQL" in result
    assert "Power BI" in result

    print("\n" + "=" * 70)
    print("✅ SEARCH TOOL TEST PASSED")
    print("=" * 70)