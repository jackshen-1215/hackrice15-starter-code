from pydantic import BaseModel
from typing import Optional

# Shared properties
class PlayerBase(BaseModel):
    name: Optional[str] = None
    team: Optional[str] = None
    position: Optional[str] = None
    points_per_game: Optional[float] = None
    rebounds_per_game: Optional[float] = None
    assists_per_game: Optional[float] = None

# Properties to receive on item creation
class PlayerCreate(PlayerBase):
    name: str
    team: str
    position: str
    points_per_game: float
    rebounds_per_game: float
    assists_per_game: float

# Properties to receive on item update
class PlayerUpdate(PlayerBase):
    pass

# Properties shared by models stored in DB
class PlayerInDBBase(PlayerBase):
    id: int
    name: str
    team: str
    position: str
    points_per_game: float
    rebounds_per_game: float
    assists_per_game: float

    class Config:
        orm_mode = True

# Properties to return to client
class Player(PlayerInDBBase):
    pass

# Properties stored in DB
class PlayerInDB(PlayerInDBBase):
    pass