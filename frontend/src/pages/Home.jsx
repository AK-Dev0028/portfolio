import { useEffect, useState } from "react";
import myPhoto from "../assets/pp.jpg";
import "./Home.css"; // Make sure your CSS is imported

export default function Home() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    // Fetch only the profile
    fetch("http://127.0.0.1:8000/api/profile")
      .then((res) => res.json())
      .then((data) => setProfile(data))
      .catch((err) => console.error("Profile fetch error:", err));
  }, []);

  if (!profile) return <div className="loading">Loading...</div>;

  return (
    <div className="container">
      {/* Profile Section */}
      <div className="profile fade-in">
        <img src={myPhoto} alt="My Photo" className="profile-pic" />
        <h1>{profile.name}</h1>
        <h2>{profile.role}</h2>
        <p className="bio">{profile.bio}</p> {/* Animated bio */}
      </div>
    </div>
  );
}
