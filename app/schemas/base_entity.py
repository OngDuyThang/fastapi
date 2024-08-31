from sqlalchemy import Column, Uuid, Time
import uuid

class BaseEntity:
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at = Column(Time, nullable=True)
    updated_at = Column(Time, nullable=True)