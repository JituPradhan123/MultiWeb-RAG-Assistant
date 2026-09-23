
from multiweb_assistant.document_loader import load_documents


def test_load_documents():

    print("=" * 70)
    print("STARTING DOCUMENT LOADER TEST")
    print("=" * 70)

    try:

        # -----------------------------------------
        # 1. Load documents
        # -----------------------------------------

        documents = load_documents()

        print(f"\nDocuments loaded: {len(documents)}")

        # -----------------------------------------
        # 2. Check documents
        # -----------------------------------------

        if not documents:
            print("\n❌ No documents were loaded.")
            return

        print("\n✅ Documents loaded successfully.\n")

        # -----------------------------------------
        # 3. Check every document
        # -----------------------------------------

        for index, document in enumerate(documents, start=1):

            print("-" * 70)
            print(f"DOCUMENT {index}")

            print("Source:")
            print(document.metadata.get("source"))

            print("\nType:")
            print(document.metadata.get("type"))

            print("\nContent length:")
            print(len(document.page_content))

            print("\nFirst 500 characters:")
            print(document.page_content[:500])

        print("-" * 70)

        print("\n✅ DOCUMENT LOADER TEST PASSED")

    except Exception as error:

        print("\n❌ DOCUMENT LOADER TEST FAILED")
        print(f"Error: {error}")

        raise


