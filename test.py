import tkinter as tk
from tkinter import scrolledtext, filedialog
from tkhtmlview import HTMLScrolledText
import markdown2

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Editor")

        # Create a frame for left and right sides
        frame = tk.Frame(root)
        frame.pack(expand=True, fill='both')

        # Create a scrolled text widget for Markdown input
        self.markdown_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=40, height=20)
        self.markdown_text.pack(side=tk.LEFT, expand=True, fill='both')

        # Create an HTML rendering widget for HTML output
        self.html_output = HTMLScrolledText(frame, wrap=tk.WORD, width=40, height=20)
        self.html_output.pack(side=tk.RIGHT, expand=True, fill='both')

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
        tk.messagebox.showinfo("About", about_message)

    def update_html_output(self, event):
        markdown_content = self.markdown_text.get(1.0, tk.END)
        html_content = markdown2.markdown(markdown_content)
        self.html_output.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    editor = MarkdownEditor(root)
    root.mainloop()
