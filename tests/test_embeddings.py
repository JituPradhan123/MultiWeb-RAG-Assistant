from multiweb_assistant.embedding import get_embedding_model


def test_get_embedding_model():

    # --------------------------------------------------
    # 1. Load embedding model
    # --------------------------------------------------

    embedding_model = get_embedding_model()

    # --------------------------------------------------
    # 2. Check model was created
    # --------------------------------------------------

    assert embedding_model is not None

    print("\n✅ Embedding model loaded successfully")

    # --------------------------------------------------
    # 3. Test single text embedding
    # --------------------------------------------------

    text = "Jitu Pradhan is a Computer Science graduate."

    embedding = embedding_model.embed_query(text)

    # --------------------------------------------------
    # 4. Check embedding was generated
    # --------------------------------------------------

    assert embedding is not None
    assert len(embedding) > 0

    print(f"Embedding dimension: {len(embedding)}")

    # --------------------------------------------------
    # 5. Check embedding values
    # --------------------------------------------------

    assert all(isinstance(value, (int, float)) for value in embedding)

    print("✅ Single text embedding generated successfully")

    # --------------------------------------------------
    # 6. Test multiple document embeddings
    # --------------------------------------------------

    texts = [
        "Python is a programming language.",
        "Django is a Python web framework.",
        "Machine learning is a branch of artificial intelligence."
    ]

    embeddings = embedding_model.embed_documents(texts)

    # --------------------------------------------------
    # 7. Check multiple embeddings
    # --------------------------------------------------

    assert embeddings is not None
    assert len(embeddings) == len(texts)

    for vector in embeddings:
        assert len(vector) == len(embedding)

    print(
        f"✅ Multiple embeddings generated successfully "
        f"for {len(texts)} documents"
    )

    print("\n" + "=" * 70)
    print("✅ EMBEDDING TEST PASSED")
    print("=" * 70)