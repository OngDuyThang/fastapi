from sqlalchemy import Boolean, Column, ForeignKey, String, Uuid
from database import Base
from schemas.base_entity import BaseEntity
from sqlalchemy.orm import relationship

class User(BaseEntity, Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    company_id = Column(Uuid, ForeignKey('companies.id'), nullable=True)
    
    company = relationship("Company", back_populates="employees")
    tasks = relationship("Task", back_populates="owner")