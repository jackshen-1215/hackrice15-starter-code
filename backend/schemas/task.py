from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True
