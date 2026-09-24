import pytest
from unittest.mock import Mock, patch

from multiweb_assistant.webpageloader import WebPageLoader


@pytest.fixture
def loader():
    return WebPageLoader([
        "https://example.com"
    ])


def test_loader_initialization(loader):
    try:
        assert loader.urls == ["https://example.com"]
        assert isinstance(loader.headers, dict)
        assert "User-Agent" in loader.headers
    except Exception as e:
        pytest.fail(f"Loader initialization test failed: {e}")


def test_clean_text(loader):
    try:
        text = """
        Hello       World

        This is     a test.

        Another line.
        """

        result = loader.clean_text(text)

        assert result == "Hello World\nThis is a test.\nAnother line."
    except Exception as e:
        pytest.fail(f"Clean text test failed: {e}")


def test_clean_text_empty(loader):
    try:
        result = loader.clean_text("")

        assert result == ""
    except Exception as e:
        pytest.fail(f"Empty text test failed: {e}")


def test_clean_html(loader):
    try:
        html = """
        <html>
            <head>
                <title>Test Page</title>
                <script>
                    console.log("test");
                </script>
            </head>
            <body>
                <header>Header</header>

                <main>
                    <h1>Machine Learning</h1>
                    <p>This is a test page.</p>
                    <p>Python and Django.</p>
                </main>

                <footer>Footer</footer>
            </body>
        </html>
        """

        result = loader.clean_html(html)

        assert "Machine Learning" in result
        assert "This is a test page." in result
        assert "Python and Django." in result
        assert "console.log" not in result
        assert "Header" not in result
        assert "Footer" not in result

    except Exception as e:
        pytest.fail(f"HTML cleaning test failed: {e}")


def test_clean_html_empty(loader):
    try:
        result = loader.clean_html("")

        assert result == ""
    except Exception as e:
        pytest.fail(f"Empty HTML test failed: {e}")


def test_fetch_success(loader):
    try:
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = 200

        with patch(
            "multiweb_assistant.webpageloader.requests.get",
            return_value=mock_response
        ) as mock_get:

            result = loader.fetch("https://example.com")

            assert result == mock_response

            mock_get.assert_called_once_with(
                "https://example.com",
                headers=loader.headers,
                timeout=20
            )

    except Exception as e:
        pytest.fail(f"Fetch success test failed: {e}")


def test_fetch_failure(loader):
    try:
        import requests

        with patch(
            "multiweb_assistant.webpageloader.requests.get",
            side_effect=requests.RequestException("Connection error")
        ):

            result = loader.fetch("https://example.com")

            assert result is None

    except Exception as e:
        pytest.fail(f"Fetch failure test failed: {e}")


def test_load_webpage(loader):
    try:
        mock_response = Mock()

        mock_response.headers = {
            "Content-Type": "text/html"
        }

        mock_response.text = """
        <html>
            <body>
                <main>
                    <h1>Test Website</h1>
                    <p>Python is a programming language.</p>
                </main>
            </body>
        </html>
        """

        with patch.object(
            loader,
            "fetch",
            return_value=mock_response
        ):

            documents = loader.load()

            assert len(documents) == 1

            document = documents[0]

            assert "Test Website" in document.page_content
            assert "Python is a programming language." in document.page_content

            assert document.metadata["source"] == "https://example.com"
            assert document.metadata["type"] == "webpage"

    except Exception as e:
        pytest.fail(f"Webpage loading test failed: {e}")


def test_load_failed_url(loader):
    try:
        with patch.object(
            loader,
            "fetch",
            return_value=None
        ):

            documents = loader.load()

            assert documents == []

    except Exception as e:
        pytest.fail(f"Failed URL test failed: {e}")


def test_load_empty_page(loader):
    try:
        mock_response = Mock()

        mock_response.headers = {
            "Content-Type": "text/html"
        }

        mock_response.text = """
        <html>
            <body></body>
        </html>
        """

        with patch.object(
            loader,
            "fetch",
            return_value=mock_response
        ):

            documents = loader.load()

            assert documents == []

    except Exception as e:
        pytest.fail(f"Empty page test failed: {e}")