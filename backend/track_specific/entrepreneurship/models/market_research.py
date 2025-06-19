from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base_class import Base

class MarketResearch(Base):
    __tablename__ = "market_research"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    industry = Column(String, index=True)
    target_audience = Column(String)
    market_size = Column(String)
    key_trends = Column(Text)

    owner = relationship("User")