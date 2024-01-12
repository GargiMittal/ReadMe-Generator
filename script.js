function generateReadMe() {
    var apiSelection = document.getElementById("apiSelection").value;
    var heading = document.getElementById("heading").value;
    var markdownContent = `# ${heading}\n\nThis ReadMe is for the ${apiSelection} API.`;

    document.getElementById("markdownContent").value = markdownContent;
    updateLivePreview(); // Call the function to update live preview
}

function updateLivePreview() {
    var markdownContent = document.getElementById("markdownContent").value;
    var previewDiv = document.getElementById("preview");
    previewDiv.innerText = markdownContent;
}
