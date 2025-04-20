import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CreateUser from './pages/CreateUser';
import UploadPost from './pages/UploadPost';
import Feed from './pages/Feed';
import React from 'react';

export default function App() {
  return (
    <Router>
      <div className="p-4 flex gap-4">
        <Link to="/">Create User</Link>
        <Link to="/upload">Upload Post</Link>
        <Link to="/feed">Feed</Link>
      </div>
      <Routes>
        <Route path="/" element={<CreateUser />} />
        <Route path="/upload" element={<UploadPost />} />
        <Route path="/feed" element={<Feed />} />
      </Routes>
    </Router>
  );
}
