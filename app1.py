import openai
import gradio as gr
import docx
openai.api_key = "your api key"
file_path="file.docx"

doc = docx.Document(file_path)
text = [p.text for p in doc.paragraphs]

dataset = []
for i, line in enumerate(text):
    if i % 2 == 0:
            # User message
         dataset.append({"role": "user", "content": line})
    else:
            # Assistant message
        dataset.append({"role": "assistant", "content": line})
    


def chatbot(input):
    if input:
        dataset.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=dataset
        )
        reply = chat.choices[0].message.content
        dataset.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
