

import gradio as gr

def create_interface(process_doc_func, query_func):
    """
    Creates and configures the Gradio web interface for the chatbot.

    Args:
        process_doc_func (function): The function to call when a document is uploaded.
        query_func (function): The function to call when a user asks a question.

    Returns:
        gradio.Blocks: The configured Gradio interface object.
    """
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="Document Q&A Chatbot"
    ) as app:
        gr.Markdown("# Document Q&A Chatbot with RAG")
        gr.Markdown("Upload a PDF or TXT file, then ask questions about its content.")

        with gr.Row():
            with gr.Column(scale=1):
                file_upload = gr.File(
                    label="Upload Document (.pdf or .txt)",
                    file_types=[".pdf", ".txt"]
                )
                upload_status = gr.Textbox(
                    label="Upload Status",
                    interactive=False,
                    placeholder="Upload a document to begin..."
                )

            with gr.Column(scale=2):
                chatbot = gr.Chatbot(
                    label="Chat",
                    bubble_full_width=False,
                    height=500
                )
                question_box = gr.Textbox(
                    label="Ask a question",
                    placeholder="Type your question here and press Enter...",
                    show_label=False
                )
                clear_button = gr.Button("Clear Chat")

        def handle_upload(file):
            if file is not None:
                return process_doc_func(file.name)
            return "No file uploaded."

        def handle_chat(question, history):
            answer = query_func(question)
            history.append((question, answer))
            return "", history # Clears the textbox and returns updated history

        file_upload.upload(
            fn=handle_upload,
            inputs=[file_upload],
            outputs=[upload_status]
        )

        question_box.submit(
            fn=handle_chat,
            inputs=[question_box, chatbot],
            outputs=[question_box, chatbot]
        )

        clear_button.click(
            fn=lambda: (None, None),
            inputs=None,
            outputs=[chatbot, question_box],
            queue=False
        )

    return app
