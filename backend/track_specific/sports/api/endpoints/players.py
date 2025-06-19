from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend.track_specific.sports import crud, models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Player])
def read_players(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[models.Player]:
    """
    Retrieve players.
    """
    players = crud.player.get_multi(db, skip=skip, limit=limit)
    return players


@router.post("/", response_model=schemas.Player)
def create_player(
    *, 
    db: Session = Depends(deps.get_db), 
    player_in: schemas.PlayerCreate
) -> models.Player:
    """
    Create new player.
    """
    player = crud.player.create(db=db, obj_in=player_in)
    return player