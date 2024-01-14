import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from tkhtmlview import HTMLScrolledText
import markdown2
import os
import replicate

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown generator")

        # Create a frame for left and right sides
        frame = tk.Frame(root)
        frame.pack(expand=True, fill='both')

        # Create an input section for API key and prompt
        input_frame = tk.Frame(frame)
        input_frame.pack(side=tk.TOP, fill='x')

        self.api_key_entry = tk.Entry(input_frame, width=40)
        self.api_key_entry.grid(row=0, column=1, padx=5, pady=5)
        api_key_label = tk.Label(input_frame, text="API Key:")
        api_key_label.grid(row=0, column=0, padx=5, pady=5)

        self.prompt_entry = tk.Entry(input_frame, width=40)
        self.prompt_entry.grid(row=1, column=1, padx=5, pady=5)
        prompt_label = tk.Label(input_frame, text="Prompt:")
        prompt_label.grid(row=1, column=0, padx=5, pady=5)

        # Create a scrolled text widget for Markdown input
        self.markdown_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=10)
        self.markdown_text.pack(side=tk.LEFT, expand=True, fill='both')

        # Create an HTML rendering widget for HTML output
        self.html_output = HTMLScrolledText(frame, wrap=tk.WORD, width=40, height=10)
        self.html_output.pack(side=tk.RIGHT, expand=True, fill='both')

        # Create a "Generate" button
        generate_button = tk.Button(input_frame, text="Generate", command=self.generate_responses)
        generate_button.grid(row=1, column=2, padx=5, pady=5)

        # Create a menu
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=root.destroy)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Bind the event to update HTML output when text is modified
        self.markdown_text.bind("<KeyRelease>", self.update_html_output)

    def save_file(self):
        content = self.markdown_text.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

    def show_about(self):
        about_message = "Markdown Editor\n\nA simple Markdown editor using Tkinter and markdown2."
        messagebox.showinfo("About", about_message)

    def update_html_output(self, event):
        markdown_content = self.markdown_text.get(1.0, tk.END)
        html_content = markdown2.markdown(markdown_content)
        self.html_output.set_html(html_content)

    def generate_responses(self):
        api_key = self.api_key_entry.get()
        prompt = self.prompt_entry.get()
        generated_text = ""
        os.environ["REPLICATE_API_TOKEN"] = api_key
        prompt=prompt
        for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 1,
            "prompt": prompt,
            "temperature": 0.5,
            "system_prompt": "your job is to genrate markdown code on prompt given.You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false informatio",
            "max_new_tokens": 500,
            "min_new_tokens": -1
            },
        ):
            generated_text += str(event)

        self.markdown_text.delete(1.0, tk.END)
        self.markdown_text.insert(tk.END, generated_text)
        
if __name__ == "__main__":
    root = tk.Tk()
    editor = MarkdownEditor(root)
    root.mainloop()
