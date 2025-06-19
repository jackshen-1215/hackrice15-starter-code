from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend.track_specific.healthcare import crud, models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Appointment])
def read_appointments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[models.Appointment]:
    """
    Retrieve appointments.
    """
    appointments = crud.appointment.get_multi(db, skip=skip, limit=limit)
    return appointments


@router.post("/", response_model=schemas.Appointment)
def create_appointment(
    *, 
    db: Session = Depends(deps.get_db), 
    appointment_in: schemas.AppointmentCreate
) -> models.Appointment:
    """
    Create new appointment.
    """
    appointment = crud.appointment.create(db=db, obj_in=appointment_in)
    return appointment