from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Allow CORS
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# API Endpoints
# -----------------------

@app.get("/api/profile")
def get_profile():
    return {
        "name": "Akhilesh Mehta",
        "email": "akhileshmehta2103@gmail.com",
        "role": "Full Stack Developer",
        "bio": "Highly motivated fresher with strong skills in Java, Spring Boot, HTML/CSS, and full-stack development. Experienced in building projects like an ERP-integrated e-commerce platform and a college management system. Eager to contribute to real-world projects and gain professional experience."
    }

@app.get("/api/projects")
def get_projects():
    return [
        {
            "title": "e-commerce website",
            "tech": ["HTML", "CSS", "Spring Boot", "Thymeleaf"],
            "year": 2025,
            "description": "Developed a full-stack e-commerce platform with ERP integration for inventory and order management."
        },
        {
            "title": "College Management System",
            "tech": ["Spring Boot", "HTML", "CSS"],
            "year": 2025,
            "description": "Designed and implemented a web application to manage students, courses, and professors efficiently."
        }
    ]

# -----------------------
# Contact POST endpoint (without email)
# -----------------------
class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/api/contact")
async def contact(c: Contact):
    # Just return the message, not sending emails
    return {"status": "ok", "msg": f"Message received from {c.name} ({c.email})"}

# -----------------------
# Serve static resume
# -----------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/resume")
def get_resume():
    return {"url": "/static/resume.pdf"}

# -----------------------
# Serve React/Vite frontend build
# -----------------------
app.mount("/", StaticFiles(directory="static/build", html=True), name="frontend")
