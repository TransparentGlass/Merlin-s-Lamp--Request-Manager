from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QFrame
from backend.Request import Request
from backend.database import databaseManager


class requestQFrame(QFrame):
    def __init__(self, request: Request, parent = None):
        super().__init__()
        uic.loadUi(r"ui\request_template.ui", self)
        self.label_date.setText(request.date)
        self.label_request_user.setText(request.author)
        self.label_requestID.setText(request.requestID)
        self.label_request_title.setText(request.title)
        self.label_request_type.setText(request.request_type)
        self.label_content.setText(request.content)

        
        
app = QApplication([])     
db = databaseManager()
result = db.fetch_requests()
for r in result:
    frame = requestQFrame(r)
    frame.show()
    
app.exec()
        
        
        
        