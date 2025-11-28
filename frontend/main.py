from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Allow development CORS
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Email configuration
# -----------------------
conf = ConnectionConfig(
    MAIL_USERNAME="yourgmail@gmail.com",        # Your Gmail
    MAIL_PASSWORD="your_app_password",         # 16-digit App Password
    MAIL_FROM="yourgmail@gmail.com",           # Sender email
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

fm = FastMail(conf)

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
# Contact POST endpoint with email sending
# -----------------------
class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/api/contact")
async def contact(c: Contact):
    message = MessageSchema(
        subject="New Message From Portfolio Contact Form",
        recipients=["yourgmail@gmail.com"],  # YOU receive the email
        body=f"""
You have a new contact form submission:

Name: {c.name}
Email: {c.email}

Message:
{c.message}
""",
        subtype="plain",
    )

    await fm.send_message(message)

    return {"status": "ok", "msg": "Email sent!"}

# -----------------------
# Serve static files (resume)
# -----------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/resume")
def get_resume():
    return {"url": "http://127.0.0.1:8000/static/resume.pdf"}
