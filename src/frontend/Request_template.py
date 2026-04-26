from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QFrame
from backend.Request import Request
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent
BACK_DIR = SRC_DIR/"backend"
ROOT_DIR = SRC_DIR.parent
UI_DIR = ROOT_DIR / "ui"

class requestQFrame(QFrame):
    def __init__(self, request: Request, parent = None):
        super().__init__(parent)
        uic.loadUi(UI_DIR / "request_template.ui", self)
        self.label_date.setText(request.date)
        self.label_request_user.setText(request.author)
        self.label_requestID.setText(request.requestID)
        self.label_request_title.setText(request.title)
        self.label_request_type.setText(request.request_type)
        self.label_content.setText(request.content)

        
        

        
        
        
        