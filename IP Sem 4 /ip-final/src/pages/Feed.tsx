import { useEffect, useState } from "react";
import { getPosts, likePost } from "../services/api";
import { Post } from "../types";
import React from "react";

export default function Feed() {
  const [posts, setPosts] = useState<Post[]>([]);

  useEffect(() => {
    getPosts().then((res) => setPosts(res.data));
  }, []);

  const handleLike = async (id: string) => {
    await likePost(id);
    setPosts((prev) =>
      prev.map((p) => (p.id === id ? { ...p, likes: p.likes + 1 } : p))
    );
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Feed</h1>
      {posts.map((post) => (
        <div key={post.id} className="border p-4 mb-2 rounded">
          <p>{post.content}</p>
          <p className="text-sm text-gray-500">Likes: {post.likes}</p>
          <button
            onClick={() => handleLike(post.id)}
            className="text-sm text-blue-600"
          >
            ❤️ Like
          </button>
        </div>
      ))}
    </div>
  );
}
