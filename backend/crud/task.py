from sqlalchemy.orm import Session
from backend.crud.base import CRUDBase
from backend.models.task import Task as TaskModel
from backend.schemas.task import TaskCreate, TaskUpdate

class CRUDTask(CRUDBase[TaskModel, TaskCreate, TaskUpdate]):
    pass

task = CRUDTask(TaskModel)
