from langchain.tools import tool

def create_search_tool(retriver):
        """Return a @tol function that search the content"""
        @tool
        def search_details(question:str)->str:
            """Search the document for information about profiles, projects,
                skills, experences , grade , certifications, extra cariculam activity """
            matching_chunks = retriver.invoke(question)
            return "\n\n".join(chunk.page_content for chunk in matching_chunks)
        return search_details
            
            