from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication
from pathlib import Path
from backend.database import databaseManager

CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent
BACK_DIR = SRC_DIR/"backend"
ROOT_DIR = SRC_DIR.parent
UI_DIR = ROOT_DIR / "ui"

class RequestSubmission(QDialog):
    def __init__(self, username, parent = None):
        super().__init__(parent)
        uic.loadUi(UI_DIR/ "Submit_request_form.ui", self)
        self.db = databaseManager()
        self.username = username
        self.pushButton_submit.clicked.connect(self.validate_and_submit)
        self.pushButton_cancel.clicked.connect(self.reject)
        
        
    def validate_and_submit(self):
        content = self.textEdit_content.toPlainText()
        title=  self.lineEdit_Title.text()
        req_type =  self.comboBox_requestType
        
        
        if content and title and req_type.activated:
            if self.db.submit_request(title, content, req_type.currentText(), self.username):
                print("Submitted successfully!")
                self.accept()
                
            else: 
                print("Submitted unsuccessfully")
                self.reject()
                
                
            
            
        
        else:
            print("Write everything")
        return
    
    
    
        
        
        