from sqlalchemy import Column, Enum, String, Numeric
from constants.enums import CompanyMode
from database import Base
from schemas.base_entity import BaseEntity
from sqlalchemy.orm import relationship

class Company(BaseEntity, Base):
    __tablename__ = "companies"
    
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    mode = Column(Enum(CompanyMode), nullable=False, default=CompanyMode.OUTSOURCE)
    rating = Column(Numeric, nullable=False, default=0)
    
    employees = relationship("User", back_populates="company")