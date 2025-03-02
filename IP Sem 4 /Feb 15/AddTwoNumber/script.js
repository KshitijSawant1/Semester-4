// Function to check if a number is even
const isEven = (a) => {
    return a % 2 === 0;
};

// Function to add two numbers
function addTwoNumber(num1, num2) {
    return num1 + num2;
}

// Function to execute both operations
function performOperations() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    let evenResult = document.getElementById("evenResult");
    let sumResult = document.getElementById("sumResult");

    if (isNaN(num1) || isNaN(num2)) {
        evenResult.textContent = "Please enter valid numbers.";
        sumResult.textContent = "";
        return;
    }

    // Check if the first number is even
    evenResult.textContent = `${num1} is ${isEven(num1) ? "Even" : "Odd"}`;

    // Add two numbers
    sumResult.textContent = `Sum: ${addTwoNumber(num1, num2)}`;
}
