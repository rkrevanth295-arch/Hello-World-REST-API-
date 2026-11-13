
from fastapi import FastAPI

app = FastAPI(title="Student Management API")

@app.get("/")
def home():
    return {
        "message": "Student Management API",
        "status": "Running"
    }
