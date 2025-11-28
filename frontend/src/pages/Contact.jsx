import { useState } from "react";
import "./Contact.css";

export default function Contact() {
  return (
    <div className="container contact-page">
      <h1 className="section-title">Contact Me</h1>

      {/* Contact Info Section */}
      <div className="contact-info">
        <p>Email: <a href="mailto:akhileshmehta2103@gmail.com">akhileshmehta2103@gmail.com</a></p>
        <p>Phone: <a href="tel:+918091798694">+91 8091798694</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/akhilesh-mehta" target="_blank" rel="noopener noreferrer">linkedin.com/in/akhilesh-mehta</a></p>
        <p>GitHub: <a href="https://github.com/akhileshmehta" target="_blank" rel="noopener noreferrer">github.com/akhileshmehta</a></p>
      </div>

      {/* Resume Download */}
      <div className="download-resume">
        <h2>Download My Resume</h2>
        <a
          href="http://127.0.0.1:8000/static/resume.pdf"
          target="_blank"
          rel="noopener noreferrer"
          download
        >
          <button>Download Resume</button>
        </a>
      </div>
    </div>
  );
}
