import pytest
from unittest.mock import Mock, patch

from multiweb_assistant import pipeline


def test_build_vector_database_existing_store():
    try:
        mock_vector_store = Mock()

        with patch(
            "multiweb_assistant.pipeline.vector_store_exists",
            return_value=True
        ), patch(
            "multiweb_assistant.pipeline.load_vector_store",
            return_value=mock_vector_store
        ):

            result = pipeline.build_vector_database_for_document()

            assert result == mock_vector_store

    except Exception as e:
        pytest.fail(
            f"Existing vector database test failed: {e}"
        )


def test_build_vector_database_new_store():
    try:
        documents = [
            Mock(page_content="Test document")
        ]

        chunks = [
            Mock(page_content="Test chunk")
        ]

        mock_vector_store = Mock()

        with patch(
            "multiweb_assistant.pipeline.vector_store_exists",
            return_value=False
        ), patch(
            "multiweb_assistant.pipeline.load_documents",
            return_value=documents
        ), patch(
            "multiweb_assistant.pipeline.split_to_chunks",
            return_value=chunks
        ), patch(
            "multiweb_assistant.pipeline.build_vector_store",
            return_value=mock_vector_store
        ), patch(
            "multiweb_assistant.pipeline.save_vector_store"
        ):

            result = pipeline.build_vector_database_for_document()

            assert result == mock_vector_store

    except Exception as e:
        pytest.fail(
            f"New vector database test failed: {e}"
        )


def test_build_vector_database_no_documents():
    try:
        with patch(
            "multiweb_assistant.pipeline.vector_store_exists",
            return_value=False
        ), patch(
            "multiweb_assistant.pipeline.load_documents",
            return_value=[]
        ):

            result = pipeline.build_vector_database_for_document()

            assert result is None

    except Exception as e:
        pytest.fail(
            f"No documents test failed: {e}"
        )


def test_build_vector_database_no_chunks():
    try:
        documents = [
            Mock(page_content="Test document")
        ]

        with patch(
            "multiweb_assistant.pipeline.vector_store_exists",
            return_value=False
        ), patch(
            "multiweb_assistant.pipeline.load_documents",
            return_value=documents
        ), patch(
            "multiweb_assistant.pipeline.split_to_chunks",
            return_value=[]
        ):

            result = pipeline.build_vector_database_for_document()

            assert result is None

    except Exception as e:
        pytest.fail(
            f"No chunks test failed: {e}"
        )


def test_build_multiweb_assistant():
    try:
        mock_vector_store = Mock()
        mock_retriever = Mock()
        mock_search_tool = Mock()
        mock_llm = Mock()
        mock_agent = Mock()

        with patch(
            "multiweb_assistant.pipeline.config.check_api_keys"
        ), patch(
            "multiweb_assistant.pipeline.build_vector_database_for_document",
            return_value=mock_vector_store
        ), patch(
            "multiweb_assistant.pipeline.get_retriever",
            return_value=mock_retriever
        ), patch(
            "multiweb_assistant.pipeline.create_search_tool",
            return_value=mock_search_tool
        ), patch(
            "multiweb_assistant.pipeline.get_llm",
            return_value=mock_llm
        ), patch(
            "multiweb_assistant.pipeline.create_multiweb_agent",
            return_value=mock_agent
        ):

            result = pipeline.build_multiweb_assistant()

            assert result == mock_agent

    except Exception as e:
        pytest.fail(
            f"Build assistant test failed: {e}"
        )


def test_build_multiweb_assistant_vector_store_failure():
    try:
        with patch(
            "multiweb_assistant.pipeline.config.check_api_keys"
        ), patch(
            "multiweb_assistant.pipeline.build_vector_database_for_document",
            return_value=None
        ):

            result = pipeline.build_multiweb_assistant()

            assert result is None

    except Exception as e:
        pytest.fail(
            f"Vector store failure test failed: {e}"
        )


def test_build_multiweb_assistant_retriever_failure():
    try:
        mock_vector_store = Mock()

        with patch(
            "multiweb_assistant.pipeline.config.check_api_keys"
        ), patch(
            "multiweb_assistant.pipeline.build_vector_database_for_document",
            return_value=mock_vector_store
        ), patch(
            "multiweb_assistant.pipeline.get_retriever",
            return_value=None
        ):

            result = pipeline.build_multiweb_assistant()

            assert result is None

    except Exception as e:
        pytest.fail(
            f"Retriever failure test failed: {e}"
        )


def test_build_multiweb_assistant_llm_failure():
    try:
        mock_vector_store = Mock()
        mock_retriever = Mock()
        mock_search_tool = Mock()

        with patch(
            "multiweb_assistant.pipeline.config.check_api_keys"
        ), patch(
            "multiweb_assistant.pipeline.build_vector_database_for_document",
            return_value=mock_vector_store
        ), patch(
            "multiweb_assistant.pipeline.get_retriever",
            return_value=mock_retriever
        ), patch(
            "multiweb_assistant.pipeline.create_search_tool",
            return_value=mock_search_tool
        ), patch(
            "multiweb_assistant.pipeline.get_llm",
            return_value=None
        ):

            result = pipeline.build_multiweb_assistant()

            assert result is None

    except Exception as e:
        pytest.fail(
            f"LLM failure test failed: {e}"
        )


def test_ask_success():
    try:
        mock_agent = Mock()

        mock_agent.invoke.return_value = {
            "messages": [
                Mock(content="This is the final answer.")
            ]
        }

        result = pipeline.ask(
            mock_agent,
            "Tell me about the project."
        )

        assert result == "This is the final answer."

        mock_agent.invoke.assert_called_once_with(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Tell me about the project."
                    }
                ]
            }
        )

    except Exception as e:
        pytest.fail(f"Ask success test failed: {e}")


def test_ask_with_none_agent():
    try:
        result = pipeline.ask(
            None,
            "Tell me about the project."
        )

        assert result == "Error: Assistant is not available."

    except Exception as e:
        pytest.fail(f"None agent test failed: {e}")


def test_ask_agent_exception():
    try:
        mock_agent = Mock()

        mock_agent.invoke.side_effect = Exception(
            "Agent invocation failed"
        )

        result = pipeline.ask(
            mock_agent,
            "Tell me about the project."
        )

        assert result == (
            "Sorry, an error occurred while processing your question."
        )

    except Exception as e:
        pytest.fail(f"Agent exception test failed: {e}")