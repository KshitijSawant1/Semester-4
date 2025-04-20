import { useEffect, useState } from "react";
import { getPosts, likePost, createPost } from "../services/api";
import { Post } from "../types";

export default function Feed() {
  const [posts, setPosts] = useState<Post[]>([]);

  const loadPosts = async () => {
    const res = await getPosts();
    if (res.data.length === 0) {
      // Add dummy posts
      await createPost({ content: "Hello from AI! 👋", userId: "1001" });
      await createPost({ content: "Check out my new post!", userId: "1002" });
      await createPost({ content: "Feeling great today 😎", userId: "1003" });

      const updatedRes = await getPosts();
      setPosts(updatedRes.data);
    } else {
      setPosts(res.data);
    }
  };

  useEffect(() => {
    loadPosts();
  }, []);

  const handleLike = async (id: string) => {
    await likePost(id);
    setPosts((prev) =>
      prev.map((p) => (p.id === id ? { ...p, likes: p.likes + 1 } : p))
    );
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <h1 className="text-3xl font-bold text-center mb-6">
        📸 InstaClone Feed
      </h1>
      <div className="max-w-xl mx-auto space-y-4">
        {posts.map((post) => (
          <div key={post.id} className="bg-white p-6 rounded-xl shadow-md">
            <div className="flex justify-between items-center mb-2">
              <div className="flex items-center gap-2">
                <div className="bg-gradient-to-r from-purple-400 to-pink-500 rounded-full h-10 w-10 flex items-center justify-center text-white font-bold">
                  {post.userId.charAt(0)}
                </div>
                <span className="text-sm text-gray-600">
                  User {post.userId}
                </span>
              </div>
              <span className="text-xs text-gray-400">
                {new Date(post.createdAt).toLocaleString()}
              </span>
            </div>
            <p className="text-gray-800 text-base mb-3">{post.content}</p>
            <div className="flex items-center justify-between">
              <button
                onClick={() => handleLike(post.id)}
                className="text-pink-500 font-semibold hover:underline"
              >
                ❤️ Like
              </button>
              <span className="text-sm text-gray-500">{post.likes} likes</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
