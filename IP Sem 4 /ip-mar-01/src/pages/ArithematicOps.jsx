import React, { useState } from "react";
import "./ArithematicsOps.css";

function ArthematicsOps() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState(null);

  const handleOperation = (operation) => {
    const number1 = parseFloat(num1);
    const number2 = parseFloat(num2);

    if (isNaN(number1) || isNaN(number2)) {
      setResult("Enter valid numbers!");
      return;
    }

    switch (operation) {
      case "add":
        setResult(number1 + number2);
        break;
      case "subtract":
        setResult(number1 - number2);
        break;
      case "multiply":
        setResult(number1 * number2);
        break;
      case "divide":
        setResult(number2 !== 0 ? number1 / number2 : "Cannot divide by zero");
        break;
      default:
        setResult(null);
    }
  };

  return (
    <div className="container">
      <h1>Arthematic Operation</h1>
      <h2>Mar 01 2025</h2>
      
      <div className="input-section">
        <input 
          type="number" 
          placeholder="Enter first number" 
          value={num1} 
          onChange={(e) => setNum1(e.target.value)} 
        />
        <input 
          type="number" 
          placeholder="Enter second number" 
          value={num2} 
          onChange={(e) => setNum2(e.target.value)} 
        />
      </div>

      <div className="button-group">
        <button onClick={() => handleOperation("add")}>Add</button>
        <button onClick={() => handleOperation("subtract")}>Subtract</button>
        <button onClick={() => handleOperation("multiply")}>Multiply</button>
        <button onClick={() => handleOperation("divide")}>Divide</button>
      </div>

      {result !== null && <div className="result">Result: {result}</div>}
    </div>
  );
}

export default ArthematicsOps;
