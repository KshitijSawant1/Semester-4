import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import CreateUser from "./pages/CreateUser";
import UploadPost from "./pages/UploadPost";
import Feed from "./pages/Feed";

export default function App() {
  return (
    <Router>
      <div className="bg-white shadow-md py-4 px-6 flex justify-center gap-10 text-lg font-medium">
        <Link to="/" className="hover:text-pink-500">
          Profile
        </Link>
        <Link to="/upload" className="hover:text-pink-500">
          Upload
        </Link>
        <Link to="/feed" className="hover:text-pink-500">
          Feed
        </Link>
      </div>
      <Routes>
        <Route path="/" element={<CreateUser />} />
        <Route path="/upload" element={<UploadPost />} />
        <Route path="/feed" element={<Feed />} />
      </Routes>
    </Router>
  );
}
