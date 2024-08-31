from models.task import TaskModel
from services.auth import token_interceptor
from database import get_db_context
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
import services.task as task_service

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(request: TaskModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return task_service.create_task(db, request)

@router.get("/", status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db_context)):
    return task_service.get_all_tasks(db)

@router.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: str, db: Session = Depends(get_db_context)):
    return task_service.get_task_by_id(db, task_id)

@router.put("/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: str, request: TaskModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return task_service.update_task(db, task_id, request)

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: str, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return task_service.delete_task(db, task_id)