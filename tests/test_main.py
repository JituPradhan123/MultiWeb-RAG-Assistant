import pytest
from unittest.mock import patch

import main


def test_main_success():
    try:
        mock_agent = object()

        with patch(
            "main.build_multiweb_assistant",
            return_value=mock_agent
        ), patch(
            "main.ask",
            return_value="Test answer"
        ) as mock_ask:

            main.main()

            assert mock_ask.call_count == 2

    except Exception as e:
        pytest.fail(f"Main success test failed: {e}")


def test_main_agent_build_failure():
    try:
        with patch(
            "main.build_multiweb_assistant",
            return_value=None
        ), patch(
            "main.ask"
        ) as mock_ask:

            main.main()

            mock_ask.assert_not_called()

    except Exception as e:
        pytest.fail(
            f"Main agent build failure test failed: {e}"
        )


def test_main_question_failure():
    try:
        mock_agent = object()

        with patch(
            "main.build_multiweb_assistant",
            return_value=mock_agent
        ), patch(
            "main.ask",
            side_effect=Exception("Question failed")
        ):

            main.main()

    except Exception as e:
        pytest.fail(
            f"Main question failure test failed: {e}"
        )


def test_main_build_exception():
    try:
        with patch(
            "main.build_multiweb_assistant",
            side_effect=Exception("Build failed")
        ):

            main.main()

    except Exception as e:
        pytest.fail(
            f"Main build exception test failed: {e}"
        )