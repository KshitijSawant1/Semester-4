import React from "react";
import "./UserProfile.css";

const UserProfile = ({ name, age, country }) => {
  return (
    <div className="profile-card">
      <h2>User Profile</h2>
      <p><strong>Name:</strong> {name}</p>
      <p><strong>Age:</strong> {age}</p>
      <p><strong>Country:</strong> {country}</p>
    </div>
  );
};

export default UserProfile;