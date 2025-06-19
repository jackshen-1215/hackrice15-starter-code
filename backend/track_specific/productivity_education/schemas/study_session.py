from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Shared properties
class StudySessionBase(BaseModel):
    user_id: Optional[int] = None
    subject: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    summary: Optional[str] = None

# Properties to receive on item creation
class StudySessionCreate(StudySessionBase):
    user_id: int
    subject: str
    start_time: datetime

# Properties to receive on item update
class StudySessionUpdate(StudySessionBase):
    pass

# Properties shared by models stored in DB
class StudySessionInDBBase(StudySessionBase):
    id: int
    user_id: int
    subject: str
    start_time: datetime

    class Config:
        orm_mode = True

# Properties to return to client
class StudySession(StudySessionInDBBase):
    pass

# Properties stored in DB
class StudySessionInDB(StudySessionInDBBase):
    pass