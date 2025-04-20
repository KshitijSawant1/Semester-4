import { useState } from "react";
import { createPost } from "../services/api";
import React from "react";

export default function UploadPost() {
  const [content, setContent] = useState("");
  const [userId, setUserId] = useState("");

  const handleSubmit = async () => {
    await createPost({ content, userId });
    alert("Post Created!");
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Create Post</h1>
      <input
        placeholder="User ID"
        className="border p-2 w-full my-2"
        onChange={(e) => setUserId(e.target.value)}
      />
      <textarea
        placeholder="Write something..."
        className="border p-2 w-full my-2"
        onChange={(e) => setContent(e.target.value)}
      />
      <button
        onClick={handleSubmit}
        className="bg-green-500 text-white px-4 py-2 rounded"
      >
        Post
      </button>
    </div>
  );
}
