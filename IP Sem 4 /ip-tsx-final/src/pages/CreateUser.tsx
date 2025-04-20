import { useState } from "react";
import { createUser } from "../services/api";

export default function CreateUser() {
  const [username, setUsername] = useState("");

  const handleSubmit = async () => {
    await createUser({ username });
    alert("User Created!");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-6">
          Create Your Profile
        </h1>
        <input
          className="w-full px-4 py-2 border rounded-md mb-4"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <button
          onClick={handleSubmit}
          className="w-full bg-gradient-to-r from-purple-500 to-pink-500 text-white font-semibold py-2 rounded-md"
        >
          Submit
        </button>
      </div>
    </div>
  );
}
