from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Allow CORS
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
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
        "bio": "Highly motivated fresher with strong skills in Java, Spring Boot, HTML/CSS..."
    }

@app.get("/api/projects")
def get_projects():
    return [
        {
            "title": "e-commerce website",
            "tech": ["HTML", "CSS", "Spring Boot", "Thymeleaf"],
            "year": 2025,
            "description": "Developed a full-stack e-commerce platform..."
        },
        {
            "title": "College Management System",
            "tech": ["Spring Boot", "HTML", "CSS"],
            "year": 2025,
            "description": "Designed and implemented a web application..."
        }
    ]

# -----------------------
# Contact POST endpoint
# -----------------------
class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/api/contact")
async def contact(c: Contact):
    return {"status": "ok", "msg": f"Message received from {c.name} ({c.email})"}
