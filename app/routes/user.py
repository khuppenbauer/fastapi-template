# app/routes/user.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..auth import authorize

router = APIRouter()

@router.get("/")
def get_users(db: Session = Depends(get_db)):
  users = db.query(models.User).all()
  return users

@router.get("/{id}")
def get_user(id: str, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).scalar()

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  return user

@router.post("/", dependencies=[Depends(authorize)])
def add_user(item: schemas.UserInput, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.name == item.name).scalar()
  
  if not user:
    user = models.User(id=uuid.uuid4(), name=item.name)
    db.add(user)
    db.commit()
    db.refresh(user)
  
  return user

@router.put("/{id}", dependencies=[Depends(authorize)])
def update_user(id: str, item: schemas.UserInput, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).scalar()

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  setattr(user, "name", item.name)
  db.commit()
  db.refresh(user)

  return user

@router.delete("/{id}", dependencies=[Depends(authorize)])
def delete_user(id: str, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).scalar()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  db.delete(user)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)
