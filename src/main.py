from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication
from frontend.request_submission import RequestSubmission

from pathlib import Path

ROOT = Path(__file__).resolve().parent
# outside src
ROOT_DIR = ROOT.parent
UI_DIR = ROOT_DIR / "ui"
QSS_PATH = ROOT_DIR / "style" / "main.qss"

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR/"merlins_lamp.ui", self)
        
        self.pushButton_add_request.clicked.connect(self.add_request)
        self.comboBox_SortPriority.currentTextChanged.connect(self.sort_Priority)
        self.comboBox_SortStatus.currentTextChanged.connect(self.sort_Status)
        self.comboBox_SortRequest.currentTextChanged.connect(self.sort_RequestType)
        
    def add_request(self):
        print("You are clicking request")
        dialog = RequestSubmission(self)    
        result = dialog.exec() 
    
        if result == QDialog.DialogCode.Accepted:
            print("User clicked OK/Submit")
        
    
    def sort_Priority(self):
        print("You're moving sort right now")
        
    def sort_RequestType(self):
        print("you're sorting to request type")
        return
    
    def sort_Status(self):
        print("You're sorting to status")
        return
    
        
        
        
        
        
# load_font()
app = QApplication([])

with open(QSS_PATH, "r") as f:
    style = f.read()
    app.setStyleSheet(style)
    
window = MyWindow()
window.show()
app.exec()