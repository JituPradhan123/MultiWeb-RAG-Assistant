from langchain.tools import tool

def create_search_tool(retriver):
    """Return a tool function that searches the content."""
    try:
        @tool
        def search_details(question: str) -> str:
            """Search the document for information about profiles, projects,
            skills, experiences, grades, certifications,
            extracurricular activities."""
            try:
                matching_chunks = retriver.invoke(question)
                return "\n\n".join(
                    chunk.page_content
                    for chunk in matching_chunks
                )
            except Exception as e:
                print(f"Error searching the content: {e}")
                return ""
        return search_details
    except Exception as e:
        print(f"Error creating search tool: {e}")
        return None