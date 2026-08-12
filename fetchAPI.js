// JavaScript Fetch API Example

// Fetch data from a public API
fetch("https://jsonplaceholder.typicode.com/users")
    .then(response => response.json())
    .then(data => {
        console.log("Users:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
