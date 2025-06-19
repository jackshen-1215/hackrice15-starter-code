from pydantic import BaseModel
from typing import Optional

# Shared properties
class MarketResearchBase(BaseModel):
    user_id: Optional[int] = None
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    market_size: Optional[str] = None
    key_trends: Optional[str] = None

# Properties to receive on item creation
class MarketResearchCreate(MarketResearchBase):
    user_id: int
    industry: str

# Properties to receive on item update
class MarketResearchUpdate(MarketResearchBase):
    pass

# Properties shared by models stored in DB
class MarketResearchInDBBase(MarketResearchBase):
    id: int
    user_id: int
    industry: str

    class Config:
        orm_mode = True

# Properties to return to client
class MarketResearch(MarketResearchInDBBase):
    pass

# Properties stored in DB
class MarketResearchInDB(MarketResearchInDBBase):
    pass