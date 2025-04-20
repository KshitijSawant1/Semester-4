import axios from "axios";

const API = axios.create({ baseURL: "http://localhost:5000/api" });

export const createUser = (user: any) => API.post("/users", user);
export const createPost = (post: any) => API.post("/posts", post);
export const getPosts = () => API.get("/posts");
export const likePost = (id: string) => API.post(`/posts/${id}/like`);

export default API;
