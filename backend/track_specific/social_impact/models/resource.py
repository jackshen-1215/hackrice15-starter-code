from sqlalchemy import Column, Integer, String
from backend.db.base_class import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    website = Column(String, nullable=True)
    description = Column(String, nullable=True)