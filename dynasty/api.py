"""
Main Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from dynasty.routes.v1 import users, fruits
import uvicorn
from trenasty.middleware.treblle import TreblleMiddleware


app = FastAPI()

app.middleware("http")(TreblleMiddleware(app))

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
app.include_router(fruits.router, prefix="/api/v1/fruits")


@app.get("/api/v1/", tags=["Root"])
async def home() -> dict:
    return {"message": "Welcome to DevDynasty API", "status": 200}
