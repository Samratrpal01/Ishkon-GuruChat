import openai
import gradio as gr
import docx
import tkinter as tk
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to the center
    window.geometry(f"{width}x{height}+{x}+{y}")

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


def on_button_click():
    user_input = entry.get()
    response=chatbot(user_input)
    label.config(text=f"Hello, {response}!")

# Create the main window
root = tk.Tk()
root.title("charbot UI")
center_window(root, 700,400)

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
root.mainloop()



inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
