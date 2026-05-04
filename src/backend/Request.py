from dataclasses import dataclass
import datetime
from enum import Enum

class StatusType(Enum):
    Unread = 0
    Working = 1
    Finished = 2
    
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    UNDEFINED = 0
    
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
    