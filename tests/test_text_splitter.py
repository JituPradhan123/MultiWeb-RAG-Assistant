from langchain_core.documents import Document

from multiweb_assistant.text_splitter import split_to_chunks
from multiweb_assistant.config import CHUNK_SIZE


def test_split_to_chunks():

    # --------------------------------------------------
    # 1. Create sample documents
    # --------------------------------------------------

    documents = [
        Document(
            page_content=(
                "Jitu Pradhan is a Computer Science graduate. "
                "He has experience with Python, Django, Machine Learning, "
                "Data Analysis, SQL, Power BI, and Generative AI. "
                "He has also worked on several software and machine learning "
                "projects during his academic career."
            ),
            metadata={
                "source": "test_document_1",
                "type": "webpage"
            }
        )
    ]

    # --------------------------------------------------
    # 2. Split documents
    # --------------------------------------------------

    chunks = split_to_chunks(documents)

    # --------------------------------------------------
    # 3. Check chunks exist
    # --------------------------------------------------

    assert chunks, "No chunks were created."

    # --------------------------------------------------
    # 4. Check number of chunks
    # --------------------------------------------------

    print(f"\nOriginal documents: {len(documents)}")
    print(f"Generated chunks: {len(chunks)}")

    assert len(chunks) >= 1

    # --------------------------------------------------
    # 5. Check every chunk
    # --------------------------------------------------

    for index, chunk in enumerate(chunks, start=1):

        print("\n" + "-" * 70)
        print(f"CHUNK {index}")

        print("\nContent:")
        print(chunk.page_content)

        print("\nContent length:")
        print(len(chunk.page_content))

        print("\nMetadata:")
        print(chunk.metadata)

        # Chunk should contain text
        assert chunk.page_content.strip(), (
            f"Chunk {index} is empty."
        )

        # Chunk should not exceed configured chunk size
        assert len(chunk.page_content) <= CHUNK_SIZE, (
            f"Chunk {index} exceeds CHUNK_SIZE."
        )

        # Metadata should be preserved
        assert chunk.metadata.get("source") == "test_document_1"

        assert chunk.metadata.get("type") == "webpage"

    print("\n" + "=" * 70)
    print("✅ TEXT SPLITTER TEST PASSED")
    print("=" * 70)