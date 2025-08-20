import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from dotenv import load_dotenv
load_dotenv()

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

def parse_document(file_path):
    """
    Parses a document based on its file extension and splits it into manageable chunks.

    Args:
        file_path (str): The path to the document file.

    Returns:
        list: A list of text chunks extracted from the document.
              Returns an empty list if the file type is unsupported or an error occurs.
    """
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == '.pdf':
        loader = PyMuPDFLoader(file_path)
    elif extension == '.txt':
        loader = TextLoader(file_path, encoding='utf-8')
    else:
        print(f"Unsupported file type: {extension}")
        return []

    try:
        print(f"Loading document: {file_path}")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        chunks = text_splitter.split_documents(documents)

        text_chunks = [chunk.page_content for chunk in chunks]
        print(f"Successfully split document into {len(text_chunks)} chunks.")
        return text_chunks

    except Exception as e:
        print(f"Error parsing document {file_path}: {e}")
        return []
