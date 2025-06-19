from sqlalchemy import Column, Integer, String, Float
from backend.db.base_class import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team = Column(String, index=True)
    position = Column(String)
    points_per_game = Column(Float)
    rebounds_per_game = Column(Float)
    assists_per_game = Column(Float)