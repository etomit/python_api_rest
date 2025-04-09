
from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str
    name: str

class UserUpdate(BaseModel):
    login: str
    password: str
    name: str
