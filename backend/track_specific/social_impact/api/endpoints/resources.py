from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.api import deps
from backend.track_specific.social_impact.crud import resource as crud_resource
from backend.track_specific.social_impact.schemas import resource as schemas_resource

router = APIRouter()

@router.post("/", response_model=schemas_resource.Resource)
def create_resource(
    *, 
    db: Session = Depends(deps.get_db),
    resource_in: schemas_resource.ResourceCreate
):
    resource = crud_resource.create_resource(db=db, resource=resource_in)
    return resource

@router.get("/", response_model=List[schemas_resource.Resource])
def read_resources(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    resources = crud_resource.get_resources(db, skip=skip, limit=limit)
    return resources