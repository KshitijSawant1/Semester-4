import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Sidebar from "./components/Sidebar/Sidebar";
import ListOptimizer from "./pages/ListOptimizer";
import UseStatePage from "./pages/UseStatePage";
import TodoList from "./pages/ToDoList";
import StopWatch from "./pages/StopWatch";
import UserProfile from "./pages/UserProfile";
import "./App.css";

function App() {
  return (
      <div className="content">
        <ListOptimizer />
        <UseStatePage />
        <TodoList />
        <StopWatch />
        <div>
          <h1>📌 User Profiles</h1>
          <UserProfile name="Kshitij K Sawant" age={22} country="India" />
          <UserProfile name="John Doe" age={28} country="USA" />
          <UserProfile name="Alice Johnson" age={25} country="UK" />
        </div>
      </div>
  );
}

export default App;
