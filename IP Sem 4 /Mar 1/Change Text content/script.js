document.getElementById("changeTextBtn").addEventListener("click", function() {
    let textElement = document.getElementById("greeting");

    if (textElement.textContent === "Hello, welcome to my webpage!") {
        textElement.textContent = "Text has been changed!";
    } else {
        textElement.textContent = "Hello, welcome to my webpage!";
    }
});


document.getElementById("changeColorBtn").addEventListener("click", function() {
    let currentColor = document.body.style.backgroundColor;
    
    if (currentColor === "rgb(186, 187, 255)") { 
        document.body.style.backgroundColor = "#f4f4f4"; // Default color
    } else {
        document.body.style.backgroundColor = "rgb(186, 187, 255)";
    }
});


document.getElementById("toggleVisibilityBtn").addEventListener("click", function() {
    let textElement = document.getElementById("greeting");

    if (textElement.classList.contains("hidden")) {
        textElement.classList.remove("hidden");
    } else {
        textElement.classList.add("hidden");
    }
});

document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();
    let errorMessage = document.getElementById("errorMessage");

    if (name === "" || email === "" || password === "") {
        errorMessage.textContent = "All fields are required!";
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        errorMessage.textContent = "Please enter a valid email!";
        return;
    }

    if (password.length < 6) {
        errorMessage.textContent = "Password must be at least 6 characters!";
        return;
    }

    errorMessage.style.color = "green";
    errorMessage.textContent = "Form submitted successfully!";
});
let counter = 0;
let counterDisplay = document.getElementById("counterDisplay");

let interval = setInterval(function() {
    if (counter < 5) {
        counter++;
        counterDisplay.textContent = "Counter: " + counter;
    } else {
        clearInterval(interval); // Stops the interval when counter reaches 5
    }
}, 5000); // Runs every 5 seconds