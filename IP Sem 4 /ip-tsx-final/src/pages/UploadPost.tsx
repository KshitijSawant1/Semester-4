import { useState } from 'react';
import { createPost } from '../services/api';

export default function UploadPost() {
  const [content, setContent] = useState('');
  const [userId, setUserId] = useState('');

  const handleSubmit = async () => {
    await createPost({ content, userId });
    alert("Post Created!");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-6">Upload a Post</h1>
        <input
          className="w-full px-4 py-2 border rounded-md mb-4"
          placeholder="User ID"
          onChange={(e) => setUserId(e.target.value)}
        />
        <textarea
          className="w-full px-4 py-2 border rounded-md mb-4"
          placeholder="Write something..."
          onChange={(e) => setContent(e.target.value)}
        />
        <button
          onClick={handleSubmit}
          className="w-full bg-gradient-to-r from-green-400 to-blue-500 text-white font-semibold py-2 rounded-md"
        >
          Post
        </button>
      </div>
    </div>
  );
}
