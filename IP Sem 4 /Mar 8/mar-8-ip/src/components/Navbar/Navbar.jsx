import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import { FaHome, FaList, FaTasks, FaStopwatch, FaUser, FaFont } from "react-icons/fa";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-brand">
        <h2>📌 React Exercises</h2>
      </div>
      <ul className="nav-links">
        <li><Link to="/"><FaHome /> Home</Link></li>
        <li><Link to="/list"><FaList /> List Optimizer</Link></li>
        <li><Link to="/useState"><FaFont /> Dynamic Font</Link></li>
        <li><Link to="/todo"><FaTasks /> To-Do List</Link></li>
        <li><Link to="/stopwatch"><FaStopwatch /> Stopwatch</Link></li>
        <li><Link to="/profile"><FaUser /> User Profile</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
