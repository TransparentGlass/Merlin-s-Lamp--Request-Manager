from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication

import backend.database as database


class RequestSubmission(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi(r"ui\Submit_request_form.ui", self)
        self.db = database.databaseManager()
        
        self.pushButton_submit.clicked.connect(self.validate_and_submit)
        self.pushButton_cancel.clicked.connect(self.reject)
        
        
    def validate_and_submit(self):
        content = self.textEdit_content.toPlainText()
        title=  self.lineEdit_Title.text()
        req_type =  self.comboBox_requestType
        
        
        if content and title and req_type.activated:
            if self.db.submit_request(title, content, req_type.currentText()):
                print("Submitted successfully!")
                
            else: 
                print("Submitted unsuccessfully")
                
                
            self.accept()
            
        
        else:
            print("Write everything")
        return
    
    
    
        
        
        