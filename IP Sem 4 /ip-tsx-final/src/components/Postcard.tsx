import React from "react";
import { Post } from "../types";
import { likePost } from "../services/api";

const PostCard: React.FC<{ post: Post }> = ({ post }) => {
  return (
    <div>
      <p>{post.content}</p>
      <p>Likes: {post.likes}</p>
      <button onClick={() => likePost(post.id)}>Like</button>
    </div>
  );
};

export default PostCard;
