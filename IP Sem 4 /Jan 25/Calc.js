function performAddition() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').textContent = 'Please enter valid numbers.';
        return;
    }

    const sum = num1 + num2;
    document.getElementById('result').textContent = `The sum is: ${sum}`;
}

function performSubtraction() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').textContent = 'Please enter valid numbers.';
        return;
    }

    const difference = num1 - num2;
    document.getElementById('result').textContent = `The difference is: ${difference}`;
}

function performMultiplication() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').textContent = 'Please enter valid numbers.';
        return;
    }

    const product = num1 * num2;
    document.getElementById('result').textContent = `The product is: ${product}`;
}

function performDivision() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').textContent = 'Please enter valid numbers.';
        return;
    }

    if (num2 === 0) {
        document.getElementById('result').textContent = 'Division by zero is not allowed.';
        return;
    }

    const quotient = num1 / num2;
    document.getElementById('result').textContent = `The quotient is: ${quotient}`;
}
