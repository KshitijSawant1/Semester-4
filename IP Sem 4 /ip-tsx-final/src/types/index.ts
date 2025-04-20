export interface User {
  id: string;
  username: string;
  bio: string;
}

export interface Post {
  id: string;
  userId: string;
  content: string;
  likes: number;
  createdAt: string;
}
