from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api import deps
from backend import crud
from backend.schemas.task import Task as TaskSchema, TaskCreate, TaskUpdate
from backend.models.task import Task as TaskModel

router = APIRouter()

@router.get("/", response_model=List[TaskSchema])
def list_tasks(db: Session = Depends(deps.get_db)) -> List[TaskModel]:
    return crud.task.get_multi(db)

@router.post("/", response_model=TaskSchema)
def create_task(task_in: TaskCreate, db: Session = Depends(deps.get_db)) -> TaskModel:
    return crud.task.create(db, obj_in=task_in)

@router.put("/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(deps.get_db)) -> TaskModel:
    db_obj = crud.task.get(db, id=task_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.task.update(db, db_obj=db_obj, obj_in=task_update.dict(exclude_unset=True))

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(deps.get_db)) -> dict:
    db_obj = crud.task.get(db, id=task_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.task.remove(db, id=task_id)
    return {"ok": True}
