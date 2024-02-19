# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import token, test

app = FastAPI()

app.include_router(test.router, prefix='/api/test')
app.include_router(token.router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {
    "message": "Welcome to the FastAPI project!"
  }
