import React from "react";
import "./Sidebar.css";

function Sidebar() {
  return (
    <div className="sidebar">
      <ul>
        <li><a href="#">🏠 Dashboard</a></li>
        <li><a href="#">📝 Tasks</a></li>
        <li><a href="#">📊 Reports</a></li>
        <li><a href="#">⚙️ Settings</a></li>
      </ul>
    </div>
  );
}

export default Sidebar;
