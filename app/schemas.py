# schemas.py
from pydantic import BaseModel

class UserInput(BaseModel):
  name: str = None
