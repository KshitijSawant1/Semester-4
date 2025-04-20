import React, { useState } from "react";
import { User } from "../types";
import { createUser } from "../services/api";

const UserForm: React.FC = () => {
  const [username, setUsername] = useState("");
  const [bio, setBio] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createUser({ username, bio });
    setUsername("");
    setBio("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create User</h2>
      <input
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        value={bio}
        onChange={(e) => setBio(e.target.value)}
        placeholder="Bio"
      />
      <button type="submit">Create</button>
    </form>
  );
};

export default UserForm;
