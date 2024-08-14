// static/js/markdown.js

// Load the Showdown library (you might also choose to include this from a CDN in your HTML file)
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/showdown@1.9.1/dist/showdown.min.js';
document.head.appendChild(script);

script.onload = function() {
    // Function to convert Markdown to HTML
    function convertMarkdownToHtml(markdownText) {
        var converter = new showdown.Converter();
        return converter.makeHtml(markdownText);
    }

    // Function to render Markdown content
    function renderMarkdown() {
        var markdownText = document.getElementById('markdown-content').innerText;
        var htmlContent = convertMarkdownToHtml(markdownText);
        document.getElementById('markdown-content').innerHTML = htmlContent;
    }

    // Wait for the DOM to fully load before running the render function
    document.addEventListener('DOMContentLoaded', renderMarkdown);
};
    