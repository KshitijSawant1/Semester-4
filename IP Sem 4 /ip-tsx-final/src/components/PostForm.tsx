import React, { useState } from "react";
import { createPost } from "../services/api";

const PostForm: React.FC<{ userId: string }> = ({ userId }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createPost({ userId, content });
    setContent("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Upload Post</h2>
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="What's on your mind?"
      />
      <button type="submit">Post</button>
    </form>
  );
};

export default PostForm;
