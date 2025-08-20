Document Q&A Chatbot 🧠
Hey there! Welcome to my little corner of the internet. This is a simple but powerful chatbot that can read through your documents (PDFs or plain text files) and answer questions about them. No more manually searching through pages of text!
It uses a cool technique called Retrieval-Augmented Generation (RAG), which basically means it's smart enough to find the exact snippets of information it needs from your documents to answer your questions accurately.
What's Inside? 🛠️
This project is built with Python and uses some awesome open-source libraries to get the job done:
LangChain: The backbone that connects everything.
OpenAI: For the powerful language model (GPT-3.5-Turbo) and embeddings.
FAISS: For super-fast searching through the document content.
Gradio: To create the simple web interface you'll be using.
Getting Started 🚀
Ready to give it a spin? It's pretty easy. Just follow these steps.
1. Clone the Repo
First things first, get the code on your machine.
git clone https://github.com/mr-sharath/document_RAG.git
cd document_RAG


2. Install the Goodies
You'll need to install all the Python packages this project depends on. I've listed them all in one command for you.
pip install gradio langchain faiss-cpu PyMuPDF openai tiktoken langchain-openai langchain-community python-dotenv


3. Set Up Your API Key
The chatbot needs an OpenAI API key to work its magic.
Create a file named .env in the main project folder.
Open it and add this one line, pasting your key inside the quotes:
OPENAI_API_KEY="sk-YourSecretKeyGoesHere"


The app will automatically load this key so you don't have to worry about it.
4. Fire It Up!
You're all set. Run the main script from your terminal:
python main.py


You'll see some messages in the terminal as it gets ready. Once it's live, it will give you a URL. Just open that link in your browser, and you're ready to chat with your documents!
How to Use It 💬
Upload a Document: Drag and drop a .pdf or .txt file into the upload box on the left.
Wait for Indexing: You'll see a status message once the file is processed and ready.
Ask Away: Type your question into the chatbox on the right and hit Enter. The bot will find the answer from the document you uploaded.
That's it! Hope you find this useful. If you have any ideas or run into issues, feel free to open an issue on GitHub.
Happy chatting!
