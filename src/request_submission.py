from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication

class RequestSubmission(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi(r"src\Submit_request_form.ui", self)
        
        self.pushButton_submit.clicked.connect(self.validate_and_submit)
        self.pushButton_cancel.clicked.connect(self.reject)
        
        
    def validate_and_submit(self):
        content = self.lineEdit_content.text()
        title=  self.lineEdit_Title.text()
        req_type =  self.comboBox_requestType
        
        if content and title and req_type.activated:
            print(self.lineEdit_content.text())
            print(title)
            self.accept()
            
        
        else:
            print("Write everything")
        return
    
        
        
        