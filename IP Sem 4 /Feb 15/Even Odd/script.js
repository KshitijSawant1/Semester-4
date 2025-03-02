function countEvenOdd() {
    const outputList = document.getElementById("outputList");
    outputList.innerHTML = ""; // Clear previous results

    for (let i = 1; i <= 10; i++) {
        const listItem = document.createElement("li");
        listItem.textContent = `${i} - ${i % 2 === 0 ? "Even" : "Odd"}`;
        listItem.className = i % 2 === 0 ? "even" : "odd";
        outputList.appendChild(listItem);
    }
}
