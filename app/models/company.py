from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

from constants.enums import CompanyMode

class CompanyModel(BaseModel):
    name: str = Field(min_length=1, max_length=99)
    description: Optional[str]
    mode: CompanyMode = Field(default=CompanyMode.OUTSOURCE)
    rating: Optional[int] = Field(default=0, ge=0, le=5)
    
class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str
    mode: CompanyMode
    rating: int
    created_at: datetime | None = None
    
    class Config:
        orm_map = True