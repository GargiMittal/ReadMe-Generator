document.addEventListener('DOMContentLoaded', function () {
    const markdownInput = document.getElementById('markdown-input');
    const markdownPreview = document.getElementById('markdown-preview');

    markdownInput.addEventListener('input', updatePreview);

    function updatePreview() {
        const markdownText = markdownInput.value;
        const htmlText = marked(markdownText);
        markdownPreview.innerHTML = htmlText;
    }
});
