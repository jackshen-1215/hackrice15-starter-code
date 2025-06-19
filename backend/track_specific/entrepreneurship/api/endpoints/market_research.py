from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend.track_specific.entrepreneurship import crud, models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.MarketResearch])
def read_market_research(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[models.MarketResearch]:
    """
    Retrieve market research.
    """
    market_research = crud.market_research.get_multi(db, skip=skip, limit=limit)
    return market_research


@router.post("/", response_model=schemas.MarketResearch)
def create_market_research(
    *, 
    db: Session = Depends(deps.get_db), 
    market_research_in: schemas.MarketResearchCreate
) -> models.MarketResearch:
    """
    Create new market research.
    """
    market_research = crud.market_research.create(db=db, obj_in=market_research_in)
    return market_research