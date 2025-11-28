import { useEffect, useState } from "react";

export default function MyWork() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_BACKEND_URL}/api/projects`)
      .then((res) => res.json())
      .then((data) => {
        setProjects(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Projects fetch error:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading projects...</p>;

  return (
    <div className="container">
      <h1 className="section-title">My Work</h1>

      <div className="projects">
        {projects.map((p, i) => (
          <div key={i} className="card slide-up">
            <h3>{p.title}</h3>
            <p className="tech">Tech: {p.tech.join(", ")}</p>
            <p className="year">Year: {p.year}</p>
            <p className="description">{p.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
