# models.py
from sqlalchemy import Column, String
from .database import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(primary_key=True, server_default='gen_random_uuid()')
  name = Column(String(255))
