import React, { useState, useEffect } from "react";
import "./InteractivePage.css"; // Separate CSS file for this page

function InteractivePage() {
  // State for text toggle, visibility, and background color
  const [text, setText] = useState("Hello, welcome to my webpage!");
  const [isHidden, setIsHidden] = useState(false);
  const [bgColor, setBgColor] = useState("#f4f4f4");

  // State for form validation
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [errorMessage, setErrorMessage] = useState("");

  // State for counter
  const [counter, setCounter] = useState(0);
  useEffect(() => {
    let interval;
    if (counter < 5) {
      interval = setInterval(() => setCounter((prev) => prev + 1), 5000);
    }
    return () => clearInterval(interval);
  }, [counter]);

  // Handlers
  const handleTextChange = () => setText(text === "Hello, welcome to my webpage!" ? "Text has been changed!" : "Hello, welcome to my webpage!");
  const handleColorChange = () => setBgColor(bgColor === "rgb(186, 187, 255)" ? "#f4f4f4" : "rgb(186, 187, 255)");
  const handleVisibilityToggle = () => setIsHidden(!isHidden);
  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  // Form validation
  const handleSubmit = (e) => {
    e.preventDefault();
    const { name, email, password } = formData;
    if (!name || !email || !password) return setErrorMessage("All fields are required!");
    if (!email.includes("@") || !email.includes(".")) return setErrorMessage("Please enter a valid email!");
    if (password.length < 6) return setErrorMessage("Password must be at least 6 characters!");
    setErrorMessage("Form submitted successfully!");
  };

  return (
    <div className="container" style={{ backgroundColor: bgColor }}>
      <h1>React Interactive Page</h1>
      
      {/* Text Toggle */}
      <p className={isHidden ? "hidden" : ""}>{text}</p>
      <button id="changeTextBtn" onClick={handleTextChange}>Change Text</button>
      <button id="changeColorBtn" onClick={handleColorChange}>Change Background Color</button>
      <button id="toggleVisibilityBtn" onClick={handleVisibilityToggle}>Toggle Visibility</button>

      {/* Form */}
      <form id="userForm" onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} />
        
        <label>Email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
        
        <label>Password:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} />
        
        <button type="submit">Submit</button>
        <p id="errorMessage" style={{ color: errorMessage.includes("success") ? "green" : "red" }}>{errorMessage}</p>
      </form>

      {/* Counter */}
      <p id="counterDisplay">Counter: {counter}</p>
    </div>
  );
}

export default InteractivePage;
