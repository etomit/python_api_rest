from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int]
    description: str
    status: str
    priority: int
    user_id: int
