import fitz  # PyMuPDF for PDFs
from ebooklib import epub
from bs4 import BeautifulSoup
import os


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return text.strip()


def extract_text_from_epub(file_path):
    """Extract text from an EPUB file."""
    text = ""
    try:
        book = epub.read_epub(file_path)
        for item in book.get_items():
            if item.get_type() == epub.EPUB_DOCUMENT:
                soup = BeautifulSoup(item.get_body_content(), "html.parser")
                text += soup.get_text() + "\n"
    except Exception as e:
        print(f"Error extracting text from EPUB: {e}")
    return text.strip()
