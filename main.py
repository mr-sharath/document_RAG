import os
from dotenv import load_dotenv
from ingestion.parser import parse_document
from retrieval.vector_store import VectorStore
from llm.query_engine import QueryEngine
import ui.app as web_ui

load_dotenv()
VECTOR_STORE_PATH = "vector_store.faiss"
def main():
    print("Initializing the RAG Chatbot...")
    print("Loading vector store...")
    vector_store = VectorStore(path=VECTOR_STORE_PATH)
    print("Vector store loaded.")

    query_engine = QueryEngine(vector_store=vector_store)
    print("Query engine initialized.")

    def process_document(file_path):
        try:
            print(f"Processing document: {file_path}")
            chunks = parse_document(file_path)
            if not chunks:
                return "Could not parse the document or it is empty."
            vector_store.add_texts(chunks)
            vector_store.save()
            print(f"Document '{os.path.basename(file_path)}' processed and indexed.")
            return f"Document '{os.path.basename(file_path)}' has been successfully indexed."
        except Exception as e:
            print(f"An error occurred during document processing: {e}")
            return f"Error processing document: {e}"

    def handle_query(question):
        try:
            print(f"Received query: {question}")
            answer = query_engine.query(question)
            print(f"Generated answer: {answer}")
            return answer
        except Exception as e:
            print(f"An error occurred during query handling: {e}")
            return f"Error answering question: {e}"

    print("Launching the web interface...")
    app = web_ui.create_interface(process_document, handle_query)
    app.launch(share=True)
    print("Web interface is live.")

if __name__ == "__main__":
    main()
