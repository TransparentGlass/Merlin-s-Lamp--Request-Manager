from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QFrame


class RequestQFrame(QFrame):
    def __init__(self, requestID, parent = None):
        super().__init__()
        uic.loadUi(r"ui\request_template.ui", self)
        
        self.requestID = requestID
        self.label_requestID.setText(f"{requestID}")
        # label_content
        # label_request_title
        # label_request_type
        # label_date
        # label_request_user
        
        
        
# app = QApplication([])     
# frame = RequestTemplate(10)
# frame.show()
# app.exec()
        
        
        
        