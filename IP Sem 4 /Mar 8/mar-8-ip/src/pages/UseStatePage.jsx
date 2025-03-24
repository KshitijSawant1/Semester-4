import React, { useState } from "react";
import "./UseStatePage.css";

function InteractivePage() {
  const [fontSize, setFontSize] = useState(16);

  const [countdown, setCountdown] = useState(10);
  const [timerActive, setTimerActive] = useState(false);
  let timer;

  const increaseFontSize = () => setFontSize(fontSize + 2);
  const decreaseFontSize = () => setFontSize(fontSize > 10 ? fontSize - 2 : 10);

  const startTimer = () => {
    if (!timerActive) {
      setTimerActive(true);
      timer = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            clearInterval(timer);
            setTimerActive(false);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
  };

  const stopTimer = () => {
    clearInterval(timer);
    setTimerActive(false);
  };

  const resetTimer = () => {
    clearInterval(timer);
    setTimerActive(false);
    setCountdown(10);
  };

  return (
    <div className="interactive-container">
      <div className="font-size-section">
        <h2 style={{ fontSize: `${fontSize}px` }}>Dynamic Font Size Adjuster</h2>
        <button onClick={increaseFontSize}>Increase Font</button>
        <button onClick={decreaseFontSize}>Decrease Font</button>
      </div>

      <div className="countdown-section">
        <h2>Countdown Timer</h2>
        <p className="countdown">{countdown}</p>
        <button onClick={startTimer} disabled={timerActive}>Start</button>
        <button onClick={stopTimer}>Stop</button>
        <button onClick={resetTimer}>Reset</button>
      </div>
    </div>
  );
}

export default InteractivePage;
