from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend.track_specific.productivity_education import crud, models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.StudySession])
def read_study_sessions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[models.StudySession]:
    """
    Retrieve study sessions.
    """
    study_sessions = crud.study_session.get_multi(db, skip=skip, limit=limit)
    return study_sessions


@router.post("/", response_model=schemas.StudySession)
def create_study_session(
    *, 
    db: Session = Depends(deps.get_db), 
    study_session_in: schemas.StudySessionCreate
) -> models.StudySession:
    """
    Create new study session.
    """
    study_session = crud.study_session.create(db=db, obj_in=study_session_in)
    return study_session