import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self, path):
        self.path = path
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = self._load_store()

    def _load_store(self):
        if os.path.exists(self.path):
            try:
                print(f"Loading existing vector store from {self.path}...")
                return FAISS.load_local(self.path, self.embeddings, allow_dangerous_deserialization=True)
            except Exception as e:
                print(f"Error loading vector store: {e}. Creating a new one.")
                return self._create_empty_store()
        else:
            print("No existing vector store found. Creating a new one.")
            return self._create_empty_store()

    def _create_empty_store(self):
        dummy_texts = ["initialize"]
        return FAISS.from_texts(dummy_texts, self.embeddings)


    def add_texts(self, texts):
        if not texts:
            print("No texts to add.")
            return
        print(f"Adding {len(texts)} new text chunks to the vector store...")
        self.vector_store.add_texts(texts)
        print("Texts added successfully.")

    def get_retriever(self, top_k=5):
        return self.vector_store.as_retriever(search_kwargs={'k': top_k})

    def save(self):
        print(f"Saving vector store to {self.path}...")
        self.vector_store.save_local(self.path)
        print("Vector store saved successfully.")
