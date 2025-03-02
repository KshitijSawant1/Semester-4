// Predefined array
const numbersArray = [10, 23, 45, 67, 89, 12, 34, 56, 78, 90];

function findNumber() {
    const userInput = parseInt(document.getElementById("userInput").value);
    const resultText = document.getElementById("result");

    if (isNaN(userInput)) {
        resultText.textContent = "Please enter a valid number.";
        return;
    }

    if (numbersArray.includes(userInput)) {
        resultText.textContent = `✅ Number ${userInput} is found in the array!`;
    } else {
        resultText.textContent = `❌ Number ${userInput} is NOT found in the array.`;
    }
}
