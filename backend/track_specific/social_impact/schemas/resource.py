from pydantic import BaseModel
from typing import Optional

class ResourceBase(BaseModel):
    name: str
    category: str
    address: str
    phone_number: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True