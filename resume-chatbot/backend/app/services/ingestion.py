"""
Data Ingestion Module - Load and chunk resume documents for RAG.
Uses LangChain's PyPDFLoader and RecursiveCharacterTextSplitter.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_data_dir() -> Path:
    """Return the absolute path to the app/data directory."""
    return Path(__file__).resolve().parent.parent / "data"


def load_and_chunk_pdf(
    filename: str = "resume.pdf",
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list:
    """
    Load a PDF from app/data/ and split it into chunks.

    Args:
        filename: Name of the PDF file in app/data/
        chunk_size: Maximum characters per chunk
        chunk_overlap: Character overlap between consecutive chunks

    Returns:
        List of Document objects with page_content and metadata
    """
    data_dir = get_data_dir()
    pdf_path = data_dir / filename

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}. "
            f"Please add your resume as '{filename}' in the app/data/ directory."
        )

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = text_splitter.split_documents(documents)
    return chunks


if __name__ == "__main__":
    # Test ingestion with resume.pdf
    print("Running data ingestion test...")
    print("-" * 50)

    try:
        chunks = load_and_chunk_pdf("resume.pdf")
        print(f"Total chunks created: {len(chunks)}")
        print("-" * 50)
        if chunks:
            print("First chunk text:")
            print(chunks[0].page_content)
            print("-" * 50)
            print("First chunk metadata:", chunks[0].metadata)
        else:
            print("No chunks created. The PDF may be empty or unreadable.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nTo test ingestion, add a resume.pdf file to backend/app/data/")
