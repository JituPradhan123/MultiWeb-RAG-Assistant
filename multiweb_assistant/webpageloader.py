import requests
from bs4 import BeautifulSoup
from io import BytesIO
from pypdf import PdfReader
from langchain_core.documents import Document


class WebPageLoader:

    def __init__(self, urls):
        self.urls = urls
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    # -----------------------------
    # Download URL
    # -----------------------------
    def fetch(self, url):
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=20
            )

            response.raise_for_status()

            return response

        except requests.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None

        except Exception as e:
            print(f"Unexpected error while fetching {url}: {e}")
            return None

    # -----------------------------
    # Extract HTML text
    # -----------------------------
    def clean_html(self, html):

        try:
            soup = BeautifulSoup(html, "lxml")

            # Remove unwanted elements
            for tag in soup([
                "script",
                "style",
                "noscript",
                "iframe",
                "svg",
                "canvas",
                "nav",
                "footer",
                "header",
                "aside",
                "form"
            ]):
                tag.decompose()

            # Find main content
            content = (
                soup.find("main")
                or soup.find("article")
                or soup.find("div", class_="content")
                or soup.body
            )

            if not content:
                return ""

            text = content.get_text(
                separator="\n",
                strip=True
            )

            return self.clean_text(text)

        except Exception as e:
            print(f"Error cleaning HTML content: {e}")
            return ""

    # -----------------------------
    # Extract PDF text
    # -----------------------------
    def clean_pdf(self, pdf_data):

        try:
            reader = PdfReader(BytesIO(pdf_data))

            pages = []

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    pages.append(text)

            return self.clean_text("\n".join(pages))

        except Exception as e:
            print(f"Error extracting PDF text: {e}")
            return ""

    # -----------------------------
    # Clean extracted text
    # -----------------------------
    def clean_text(self, text):

        try:
            lines = []

            for line in text.splitlines():

                line = " ".join(line.split())

                if line:
                    lines.append(line)

            return "\n".join(lines)

        except Exception as e:
            print(f"Error cleaning text: {e}")
            return ""

    # -----------------------------
    # Load all URLs
    # -----------------------------
    def load(self):

        documents = []

        try:

            for url in self.urls:

                try:

                    response = self.fetch(url)

                    if response is None:
                        continue

                    # Detect file type
                    content_type = response.headers.get(
                        "Content-Type",
                        ""
                    ).lower()

                    # -----------------------------
                    # PDF
                    # -----------------------------
                    if (
                        "application/pdf" in content_type
                        or url.lower().endswith(".pdf")
                    ):

                        text = self.clean_pdf(
                            response.content
                        )

                        document_type = "pdf"

                    # -----------------------------
                    # HTML webpage
                    # -----------------------------
                    else:

                        text = self.clean_html(
                            response.text
                        )

                        document_type = "webpage"

                    # -----------------------------
                    # Create LangChain Document
                    # -----------------------------
                    if text:

                        documents.append(
                            Document(
                                page_content=text,
                                metadata={
                                    "source": url,
                                    "type": document_type
                                }
                            )
                        )

                        print(f"Loaded: {url}")

                    else:

                        print(f"No text found: {url}")

                except requests.RequestException as e:

                    print(f"Failed to load {url}: {e}")

                except Exception as e:

                    print(f"Error processing {url}: {e}")

        except Exception as e:

            print(f"Error loading URLs: {e}")

        return documents