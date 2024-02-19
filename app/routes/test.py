# app/routes/test.py
from fastapi import APIRouter, Depends
from ..auth import authorize

router = APIRouter()

@router.get("/")
def get():
  return {"status": "ok"}

@router.post("/", dependencies=[Depends(authorize)])
def post():
  return {"status": "ok"}  
