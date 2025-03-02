function countNumbers() {
    const arr = [1, -3, 0, 5, -2, 0, 9, -7, 0];
    let zeroCount = 0, positiveCount = 0, negativeCount = 0;

    for (let num of arr) {
        if (num === 0) {
            zeroCount++;
        } else if (num > 0) {
            positiveCount++;
        } else {
            negativeCount++;
        }
    }

    const resultText = `Zeros: ${zeroCount}, Positives: ${positiveCount}, Negatives: ${negativeCount}`;
    document.getElementById("result").textContent = resultText;
}
