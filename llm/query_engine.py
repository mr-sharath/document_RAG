from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class QueryEngine:
    def __init__(self, vector_store):
        self.retriever = vector_store.get_retriever()
        self.llm = self._initialize_llm()
        self.qa_chain = self._initialize_qa_chain()

    def _initialize_llm(self):
        print("Initializing the language model (OpenAI GPT-3.5 Turbo)...")
        return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    def _initialize_qa_chain(self):
        prompt_template = """
        You are a helpful assistant. Your task is to answer the user's question based ONLY on the provided context.
        If the information to answer the question is not in the context, you MUST say: "Not found in document".
        Do not add any information that is not in the context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        print("Setting up the RetrievalQA chain...")
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )

    def query(self, question):
        if not question:
            return "Please ask a question."

        print(f"Executing query: {question}")
        result = self.qa_chain({"query": question})

        answer = result.get('result', "Sorry, I couldn't find an answer.")
        print(f"Query result: {answer}")
        return answer
