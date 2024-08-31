from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    
class CompanyMode(Enum):
    OUTSOURCE = "outsource"
    PRODUCT = "product"
    
class TaskStatus(Enum):
    BACKLOG = "backlog"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    
class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"