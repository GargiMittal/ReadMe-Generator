# Markdown Generator

This is a simple AI integrated Markdown generator implemented in Python using the Tkinter library for the graphical user interface and the `tkhtmlview`, `replicate`, and `markdown2` libraries for HTML rendering, text generation, and Markdown conversion, respectively.

## Getting Started

To use this Markdown generator, you need to have Python installed on your system.

1. **Clone the repository or download the source code:**

    ```bash
    git clone https://github.com/gargimittal/ReadMe-generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ReadMe-generator
    ```

3. **Install the required Python packages:**

    ```bash
    pip install markdown2
    pip install replicate
    ```

4. **Run the Markdown generator:**

    ```bash
    python mdGenrator.py
    ```

## Features

- **Markdown Input:** Enter your Markdown content in the left pane using the provided ScrolledText widget.

- **HTML Output:** View the HTML-rendered output in the right pane using the HTMLScrolledText widget.

- **Generate Responses:** Generate Markdown content using the provided API key and prompt. Click the "Generate" button to fetch responses based on the specified settings.

- **Save File:** Save the entered Markdown content to a file by clicking on "File" in the menu and selecting "Save."

- **About:** Learn more about the Markdown editor by clicking on "Help" in the menu and selecting "About."

## Usage Instructions


1. Enter your API key and prompt in the designated input fields.

2. Click the "Generate" button to populate the Markdown pane with responses based on the provided API key and prompt.

3. Input your Markdown content or make changes in the left pane.

4. Save your Markdown content by selecting "File" and then "Save" from the menu.

## Contributions

Feel free to contribute to the development of this Markdown generator by submitting issues or pull requests. Your feedback and contributions are highly appreciated.

## Acknowledgments

- This project utilizes the Tkinter, tkhtmlview, replicate, and markdown2 libraries.
- Special thanks to the developers of replicate for providing the API used for text generation.

---

**Note:** Make sure to keep your API key secure and do not share it publicly. The API key is sensitive information and should be handled with care.
