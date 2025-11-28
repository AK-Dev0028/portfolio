import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import MyWork from "./pages/Mywork";
import Contact from "./pages/Contact";
import SkillsPage from "./pages/Skills";
import "./App.css";

export default function App() {
  return (
    <Router>
      <nav className="navbar">
        <Link to="/">Home</Link>
        <Link to="/mywork">My Work</Link>
        <Link to="/contact">Contact</Link>
        <Link to="/skills">Skill</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/mywork" element={<MyWork />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/skills" element={<SkillsPage />} />
      </Routes>
    </Router>
  );
}
