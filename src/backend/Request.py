from dataclasses import dataclass
import datetime
from enum import Enum

class StatusType(Enum):
    ONGOING = "On-going"
    UNREAD = "Unread"
    FINISHED = "Finished"
    
class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    UNDEFINED = None
    
@dataclass
class Request:
    title: str
    request_type: str
    priority: Priority
    status: StatusType
    content: str
    date: datetime
    authorID: int
    requestID: int = None
    
    @property
    def formatted_date(self):
        return self.date.strftime("%d/%m/%y")
    
    def get_priority(val):
        return Priority(val) if val is not None else Priority.LOW

    def get_status(val):
        return StatusType(val) if val is not None else StatusType.UNREAD