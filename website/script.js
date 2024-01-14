const editor = document.querySelector('.markdown-editor');
const preview = document.querySelector('.live-preview');

editor.addEventListener('input', (e) => {
    console.log(e.target.value);
    preview.innerHTML = DOMPurify.sanitize(marked.parse(e.target.value));
});

async function generateReadMe() {
    const apiKey = document.getElementById('apiSelection').value;
    const promptText = document.getElementById('heading').value;

    // Initialize Replicate with API key
    const replicate = new Replicate({
        auth: apiKey,
    });

    // Run meta/llama-2-70b-chat using Replicate’s API
    const input = {
        debug: false,
        top_k: 50,
        top_p: 1,
        prompt: promptText,
        temperature: 0.5,
        system_prompt: "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.you will only answer in markdown code and your main purpose is to genrate read me files. If you don't know the answer to a question, please don't share false information",
        max_new_tokens: 500,
        min_new_tokens: -1
    };

    // Stream events and update markdown editor
    for await (const event of replicate.stream("meta/llama-2-70b-chat", { input })) {
        const generatedContent = event.toString();
        document.getElementById('markdownContent').value = generatedContent;
        // You can also update the live preview if needed
        document.getElementById('preview').innerHTML = DomPurify.sanitize(marked.parse(generatedContent));
    }
}