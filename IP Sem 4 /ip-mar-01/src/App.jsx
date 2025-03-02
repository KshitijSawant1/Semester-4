import React from "react";
import ArithematicOps from "./pages/ArithematicOps";
import Navbar from "./component/Navbar/navbar";
import Sidebar from "./component/SideBar/sidebar"; // Import Sidebar
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <Sidebar />
      <div className="content">
        <ArithematicOps />
      </div>
    </div>
  );
}

export default App;
