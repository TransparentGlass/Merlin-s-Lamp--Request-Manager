from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication
from frontend.request_submission import RequestSubmission
from backend.Request import Request, Priority, StatusType
from backend.database import databaseManager
from frontend.request_template import requestQFrame 

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
        self.stackedWidget.setCurrentIndex(0)
        
        self.db = databaseManager()
        self.load_request()
        
        self.pushButton_userLogIn.clicked.connect(self.userLogIn)
        self.pushButton_AdminSignIn.clicked.connect(self.adminLogin)
        self.pushButton_register.clicked.connect(self.userRegister)
        
        self.btn_apply_filter.clicked.connect(self.apply_filter)
        self.pushButton_add_request.clicked.connect(self.add_request)
        self.comboBox_SortPriority.currentTextChanged.connect(self.filter_Priority)
        self.comboBox_SortStatus.currentTextChanged.connect(self.filter_Status)
        self.comboBox_SortRequest.currentTextChanged.connect(self.sort_RequestType)
        
        self.filter_type = None
        self.filter_prio = None
        self.filter_status = None
        
         
         
    def userRegister(self) -> bool:
        self.username = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        if self.db.userRegister(self.username, self.password):
            print("Successfully registered. Log in to account")
            return True
        
        return False
    
    def userLogIn(self) -> bool:
        self.username = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        if self.db.userLogin(self.username, self.password):
            print(f"welcome {self.username}")
            self.stackedWidget.setCurrentIndex(1)
            self.showMaximized()
            return True
        
        return False
    
    def adminLogin(self): pass
            
    def add_request(self):
        print("You are clicking request")
        dialog = RequestSubmission(self.username, self)    
        result = dialog.exec() 
    
        if result == QDialog.DialogCode.Accepted:
            print("User clicked OK/Submit")
            self.update_requests()
            
    def load_request(self, requests = None) -> bool:
        if requests:
            self.requests = requests
        else:
            self.requests = self.db.fetch_requests()
            
        if not self.requests:
            print("Request is empty or error")
            return False;
        
        requests_frame = self.frame_allRequests.layout()
            
        for r in self.requests:
            widget = requestQFrame(r, self)
            requests_frame.addWidget(widget)
        return True
                  
    def update_requests(self, requests = None) -> bool:
        self.clear_layout()
        if requests:
            self.load_request(requests)
        else:
            self.load_request()
        
            
    def clear_layout(self):
        layout = self.frame_allRequests.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
    def apply_filter(self):
        newFiltered = self.db.fetch_requests(self.filter_prio, self.filter_status, self.filter_type)      
        self.update_requests(newFiltered)  
                
        
        
    def filter_Priority(self):
        ui_text = self.comboBox_SortPriority.currentText().strip().upper()
        if ui_text != "ALL":
            self.filter_prio = ui_text
        else:
            self.filter_prio = None
        
        print(f"Sorting via priority {self.filter_prio}")   
        
    def filter_Status(self):
        ui_text = self.comboBox_SortStatus.currentText().strip()
        if ui_text != "ALL":
            self.filter_status = ui_text
        else:
            self.filter_status = None
            
        print(f"Sorting via Status {self.filter_status}")
        
        
    def sort_RequestType(self):
        ui_text = self.comboBox_SortRequest.currentText().strip()
        if ui_text != "ALL":
            self.filter_type = ui_text
        else:
            self.filter_type = None
            
        print(f"Sorting via requestType {self.filter_type}")
    
        
        
        
        
        
# load_font()
app = QApplication([])

with open(QSS_PATH, "r") as f:
    style = f.read()
    app.setStyleSheet(style)
    
window = MyWindow()
window.show()
app.exec()