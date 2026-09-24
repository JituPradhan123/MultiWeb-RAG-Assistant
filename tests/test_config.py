import pytest
from multiweb_assistant import config


def test_config_urls():
    try:
        assert isinstance(config.urls, list)
        assert len(config.urls) > 0
    except Exception as e:
        pytest.fail(f"Config URLs test failed: {e}")


def test_config_vector_store_path():
    try:
        assert isinstance(config.VECTOR_STORE_PATH, str)
        assert len(config.VECTOR_STORE_PATH) > 0
    except Exception as e:
        pytest.fail(f"Vector store path test failed: {e}")


def test_config_chunk_size():
    try:
        assert isinstance(config.CHUNK_SIZE, int)
        assert config.CHUNK_SIZE > 0
    except Exception as e:
        pytest.fail(f"Chunk size test failed: {e}")


def test_config_chunk_overlap():
    try:
        assert isinstance(config.CHUNK_OVERLAP, int)
        assert config.CHUNK_OVERLAP >= 0
        assert config.CHUNK_OVERLAP < config.CHUNK_SIZE
    except Exception as e:
        pytest.fail(f"Chunk overlap test failed: {e}")


def test_config_top_k_results():
    try:
        assert isinstance(config.TOP_K_RESULTS, int)
        assert config.TOP_K_RESULTS > 0
    except Exception as e:
        pytest.fail(f"TOP_K_RESULTS test failed: {e}")


def test_config_embedding_model():
    try:
        assert isinstance(config.EMBEDDING_MODEL_NAME, str)
        assert len(config.EMBEDDING_MODEL_NAME) > 0
    except Exception as e:
        pytest.fail(f"Embedding model config test failed: {e}")


def test_config_llm_model():
    try:
        assert isinstance(config.LLM_MODEL_NAME, str)
        assert len(config.LLM_MODEL_NAME) > 0
    except Exception as e:
        pytest.fail(f"LLM model config test failed: {e}")


def test_check_api_keys():
    try:
        result = config.check_api_keys()
        assert result is None
    except Exception as e:
        pytest.fail(f"API key check failed: {e}")