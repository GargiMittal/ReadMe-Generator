const editor = document.querySelector('.markdown-editor');
const preview = document.querySelector('.live-preview');

editor.addEventListener('input', (e) => {
    console.log(e.target.value);
    preview.innerHTML = DOMPurify.sanitize(marked.parse(e.target.value));
});
