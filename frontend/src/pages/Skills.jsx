import React from "react";
import "./Skills.css"; // Make sure this file exists

export default function SkillsPage() {
  const skills = [
    { category: "Programming Languages", items: ["Java", "Python"] },
    { category: "Backend", items: ["Spring Boot", "Django", "Hibernate", "REST APIs"] },
    { category: "Frontend", items: ["HTML", "CSS", "React", "Thymeleaf"] },
    { category: "Core Concepts", items: ["OOPs"] },
    { category: "Tools & Others", items: ["Git", "GitHub", "MySQL"] }
  ];

  return (
    <div className="skills-container">

      {/* Header */}
      <header className="skills-header">
        <h1>My Skills</h1>
        <p>A collection of my technical skills, tools, and technologies I work with.</p>
      </header>

      {/* Grid */}
      <div className="skills-grid">
        {skills.map((skill, idx) => (
          <div key={idx} className="skill-card">
            <h2>{skill.category}</h2>
            <ul>
              {skill.items.map((item, i) => (
                <li key={i}>
                  <span className="skill-dot"></span> {item}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      {/* Footer */}
      <footer className="skills-footer">
        © {new Date().getFullYear()} Akhilesh Mehta. All rights reserved.
      </footer>

    </div>
  );
}
