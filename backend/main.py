from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Allow CORS
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Serve static files (resume)
# -----------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------
# API Endpoints
# -----------------------
@app.get("/api/profile")
def get_profile():
    return {
        "name": "Akhilesh Mehta",
        "email": "akhileshmehta2103@gmail.com",
        "role": " Developer",
        "bio": (
            "Highly motivated fresher with strong skills in Java, Spring Boot, HTML/CSS, "
            "JavaScript, React, and other modern web technologies. Passionate about developing "
            "efficient and user-friendly web applications. Experienced in building full-stack projects, "
            "integrating RESTful APIs, and working with databases. Eager to contribute to innovative projects "
            "and continuously learn new technologies in a collaborative environment."
        ),
        # Resume URL exposed to frontend
        "resume_url": "/static/resume.pdf"
    }

@app.get("/api/projects")
def get_projects():
    return [
        {
            "title": "E-commerce Website",
            "tech": ["HTML", "CSS", "Spring Boot", "Thymeleaf"],
            "year": 2025,
            "description": "Developed a full-stack e-commerce platform with product listings, shopping cart, and order management."
        },
        {
            "title": "College Management System",
            "tech": ["Spring Boot", "HTML", "CSS"],
            "year": 2025,
            "description": "Designed and implemented a web application for managing student records, courses, and faculty data."
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

# -----------------------
# Optional: Root endpoint
# -----------------------
@app.get("/")
def root():
    return {"message": "Welcome to Akhilesh Mehta Portfolio Backend"}
