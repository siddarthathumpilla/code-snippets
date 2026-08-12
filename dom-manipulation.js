// JavaScript DOM Manipulation Example

// Find an element by ID
const heading = document.getElementById("heading");

// Change the text
heading.textContent = "Hello, JavaScript!";

// Change the color
heading.style.color = "blue";

// Add a click event
heading.addEventListener("click", function () {
    alert("Heading clicked!");
});
