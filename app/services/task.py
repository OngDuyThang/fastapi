from datetime import datetime
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.task import TaskModel
from schemas.task import Task

def create_task(db: Session, request: TaskModel):
    if (not request.summary) or (not request.description) or (not request.status) or (not request.priority):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    try:
        newTask = Task(**request.model_dump())
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
        return newTask
    except Exception as e:
        raise HTTPException(e)
    
def get_all_tasks(db: Session):
    try:
        return db.query(Task).all()
    except Exception as e:
        raise HTTPException(e)
    
def get_task_by_id(db: Session, task_id: UUID):
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return task
    except Exception as e:
        raise HTTPException(e)
    
def update_task(db: Session, task_id: UUID, request: TaskModel):
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task.summary = request.summary
        task.description = request.description
        task.status = request.status
        task.priority = request.priority
        task.updated_at = datetime.now()
        
        db.add(task)
        db.commit()
        db.refresh(task)
        
        return task
    except Exception as e:
        raise HTTPException(e)
    
def delete_task(db: Session, task_id: UUID):
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        db.delete(task)
        db.commit()
        
        return True
    except Exception as e:
        raise HTTPException(e)