from sqlalchemy.orm import Session
from .models import Resource
from .schemas import ResourceCreate

def get_resource(db: Session, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def get_resources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Resource).offset(skip).limit(limit).all()

def create_resource(db: Session, resource: ResourceCreate):
    db_resource = Resource(**resource.dict())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource