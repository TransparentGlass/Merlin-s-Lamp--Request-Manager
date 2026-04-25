from PyQt6.QtWidgets import QFrame
from Request_template import RequestQFrame

class Request:
    def __init__(self, title, request_type, content, date, author, requestID = None, parent = None):
        super().__init__(parent)
        self.title = title
        self.request_type = request_type
        self.content = content
        self.date = date
        self.author = author
        self.ReqID = requestID
        
        
        
    def create_request_frame(self):
        
        return
    
        
        