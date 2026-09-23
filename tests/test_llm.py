from multiweb_assistant.llm import get_llm


def test_get_llm():

    # --------------------------------------------------
    # 1. Create LLM
    # --------------------------------------------------

    llm = get_llm()

    # --------------------------------------------------
    # 2. Check LLM object
    # --------------------------------------------------

    assert llm is not None

    print("\n✅ LLM initialized successfully")

    # --------------------------------------------------
    # 3. Test actual LLM response
    # --------------------------------------------------

    response = llm.invoke(
        "Say hello in one short sentence."
    )

    # --------------------------------------------------
    # 4. Check response
    # --------------------------------------------------

    assert response is not None

    print("\nLLM Response:")
    print(response.content)

    assert response.content
    assert len(response.content.strip()) > 0

    print("\n✅ LLM generated a response successfully")

    print("\n" + "=" * 70)
    print("✅ LLM TEST PASSED")
    print("=" * 70)