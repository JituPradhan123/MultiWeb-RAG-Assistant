from langchain_core.documents import Document

from multiweb_assistant.vector_store import (
    build_vector_store,
    save_vector_store,
    vector_store_exists,
    load_vector_store,
    get_retriever,
)


def test_vector_store():

    # --------------------------------------------------
    # 1. Create test documents
    # --------------------------------------------------

    documents = [
        Document(
            page_content=(
                "Jitu Pradhan is a Computer Science graduate "
                "with experience in Python and Django."
            ),
            metadata={
                "source": "test_resume",
                "type": "webpage",
            },
        ),
        Document(
            page_content=(
                "Jitu has experience with Machine Learning, "
                "Data Analysis, SQL and Power BI."
            ),
            metadata={
                "source": "test_resume",
                "type": "webpage",
            },
        ),
        Document(
            page_content=(
                "Jitu has developed projects using Django, "
                "Machine Learning and Generative AI."
            ),
            metadata={
                "source": "test_resume",
                "type": "webpage",
            },
        ),
    ]

    # --------------------------------------------------
    # 2. Build vector store
    # --------------------------------------------------

    vector_store = build_vector_store(documents)

    assert vector_store is not None

    print("\n✅ Vector store created successfully")

    # --------------------------------------------------
    # 3. Check number of stored documents
    # --------------------------------------------------

    count = vector_store._collection.count()

    print(f"Stored documents: {count}")

    assert count == len(documents)

    # --------------------------------------------------
    # 4. Test similarity search
    # --------------------------------------------------

    query = "What programming technologies does Jitu know?"

    results = vector_store.similarity_search(
        query,
        k=2,
    )

    print("\nSimilarity search results:")

    for index, result in enumerate(results, start=1):

        print("\n" + "-" * 60)
        print(f"RESULT {index}")
        print(result.page_content)

    assert results
    assert len(results) <= 2

    # --------------------------------------------------
    # 5. Test save
    # --------------------------------------------------

    save_vector_store(vector_store)

    print("\n✅ Vector store saved successfully")

    # --------------------------------------------------
    # 6. Check vector store exists
    # --------------------------------------------------

    exists = vector_store_exists()

    print(f"Vector store exists: {exists}")

    assert exists is True

    # --------------------------------------------------
    # 7. Load vector store
    # --------------------------------------------------

    loaded_vector_store = load_vector_store()

    assert loaded_vector_store is not None

    print("✅ Vector store loaded successfully")

    # --------------------------------------------------
    # 8. Check loaded database
    # --------------------------------------------------

    loaded_count = loaded_vector_store._collection.count()

    print(f"Loaded document count: {loaded_count}")

    assert loaded_count == len(documents)

    # --------------------------------------------------
    # 9. Test retriever
    # --------------------------------------------------

    retriever = get_retriever(
        loaded_vector_store,
        k=2,
    )

    assert retriever is not None

    retrieved_documents = retriever.invoke(
        "Tell me about Jitu's Django experience."
    )

    print("\nRetriever results:")

    for index, document in enumerate(
        retrieved_documents,
        start=1,
    ):

        print("\n" + "-" * 60)
        print(f"RETRIEVED CHUNK {index}")
        print(document.page_content)

    assert retrieved_documents
    assert len(retrieved_documents) == 2

    print("\n" + "=" * 70)
    print("✅ VECTOR STORE TEST PASSED")
    print("=" * 70)