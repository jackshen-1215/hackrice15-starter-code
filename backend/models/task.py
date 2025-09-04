from sqlalchemy import Column, Integer, String, Boolean
from backend.db.base_class import Base

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
