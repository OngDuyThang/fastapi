from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from constants.enums import TaskPriority, TaskStatus
    
class TaskModel(BaseModel):
    summary: Optional[str]
    description: Optional[str]
    status: TaskStatus = Field(default=TaskStatus.BACKLOG)
    priority: TaskPriority = Field(default=TaskPriority.LOW)
    owner_id: Optional[UUID]
    
class TaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime | None = None
    
    class Config:
        orm_map = True