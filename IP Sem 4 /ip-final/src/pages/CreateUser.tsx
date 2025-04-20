import { useState } from "react";
import { createUser } from "../services/api";
import React from "react";

export default function CreateUser() {
  const [username, setUsername] = useState("");

  const handleSubmit = async () => {
    await createUser({ username });
    alert("User Created!");
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Create User</h1>
      <input
        className="border p-2 my-2 w-full"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Submit
      </button>
    </div>
  );
}
