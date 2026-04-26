from dataclasses import dataclass
import datetime
@dataclass
class Request:
    title: str
    request_type: str
    content: str
    date: datetime
    author: str
    requestID: int = None
    
    @property
    def formatted_date(self):
        return self.date.strftime("%d/%m/%y")