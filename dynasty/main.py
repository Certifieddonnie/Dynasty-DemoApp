"""
Main Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.v1 import users


app = FastAPI()

origins = [
    # "https://devdynasty.netlify.app",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api/v1")


@app.get("/")
async def home():
    return {"message": "Welcome to DevDynasty API", "status": 200}
