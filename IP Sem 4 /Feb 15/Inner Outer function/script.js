function outerFunction() {
    console.log("The Outer function is called.");

    function innerFunction() {
        alert("Hello, KS! This is the inner function.");
    }

    innerFunction();
}

document.getElementById("myButton").addEventListener("click", outerFunction);
