document.addEventListener("DOMContentLoaded", function () {
    const markdownContent = document.getElementById("markdownContent");
    const preview = document.getElementById("preview");

    function updateLivePreview() {
        const markdownText = markdownContent.value;
        const htmlText = marked(markdownText);
        preview.innerHTML = htmlText;
    }

    // Add the event listener after declaring markdownContent
    markdownContent.addEventListener("input", updateLivePreview);

    function generateReadMe() {
        var apiSelection = document.getElementById("apiSelection").value;
        var heading = document.getElementById("heading").value;
        var markdownContent = `# ${heading}\n\nThis ReadMe is for the ${apiSelection} API.`;

        document.getElementById("markdownContent").value = markdownContent;
        updateLivePreview(); // Call the function to update live preview
    }
});
