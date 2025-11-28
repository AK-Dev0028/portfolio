from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import FileResponse, JSONResponse
import os

app = FastAPI()

# ----------------------- CORS -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://portfolio-mehta.onrender.com"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------- Serve static files -----------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# ----------------------- API Endpoints -----------------------
@app.get("/api/profile")
def get_profile():
    return {"name": "Akhilesh Mehta", "email": "akhileshmehta2103@gmail.com", "role": "Developer"}

@app.get("/api/projects")
def get_projects():
    return [
        {"title": "E-commerce Website", "year": 2025},
        {"title": "College Management System", "year": 2025}
    ]

class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/api/contact")
async def contact(c: Contact):
    return {"status": "ok", "msg": f"Message received from {c.name}"}

# ----------------------- Serve React SPA -----------------------
@app.get("/", response_class=FileResponse)
def serve_react():
    return FileResponse("static/index.html", media_type="text/html")

@app.get("/{full_path:path}", response_class=FileResponse)
def catch_all(full_path: str):
    if full_path.startswith("api"):
        return JSONResponse(status_code=404, content={"detail": "API route not found"})
    return FileResponse("static/index.html", media_type="text/html")
