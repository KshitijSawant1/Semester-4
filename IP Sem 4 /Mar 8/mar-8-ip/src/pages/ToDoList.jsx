import React, { useReducer, useState } from "react";

const initialState = [];

const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_TASK":
      return [...state, action.payload];
    case "REMOVE_TASK":
      return state.filter((task, index) => index !== action.payload);
    default:
      return state;
  }
};

const ToDoList = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const [task, setTask] = useState("");

  const addTask = () => {
    if (task.trim() !== "") {
      dispatch({ type: "ADD_TASK", payload: task });
      setTask("");
    }
  };

  return (
    <div className="todo-container">
      <h2>📌 To-Do List</h2>
      <input 
        type="text" 
        value={task} 
        onChange={(e) => setTask(e.target.value)} 
        placeholder="Enter task..." 
      />
      <button onClick={addTask}>Add Task</button>
      <ul>
        {state.map((task, index) => (
          <li key={index}>
            {task} 
            <button onClick={() => dispatch({ type: "REMOVE_TASK", payload: index })}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ToDoList;
