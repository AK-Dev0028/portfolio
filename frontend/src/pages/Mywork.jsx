import { useEffect, useState } from "react";

export default function MyWork() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/projects")
      .then((res) => res.json())
      .then((data) => {
        setProjects(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading projects...</p>;

  return (
    <div className="container">
      <h1 className="section-title">My Work</h1>

      <div className="projects">
        {projects.map((p, i) => (
          <div key={i} className="card slide-up">
            <h3>{p.title}</h3>

            {/* FIX: tech array displayed correctly */}
            <p className="tech">Tech: {p.tech.join(", ")}</p>

            <p className="year">Year: {p.year}</p>

            {/* FIX: using real backend description */}
            <p className="description">{p.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
