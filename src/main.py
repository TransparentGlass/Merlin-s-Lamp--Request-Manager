from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QMessageBox
from frontend.request_submission import RequestSubmission
from backend.Request import Request, Priority, StatusType
from backend.database import databaseManager
from frontend.admin_user_request_template import adminQFrame, userQFrame
from frontend.register_page import RegisterPage

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent #Current Directory SRC
ROOT_DIR = BASE_DIR.parent #THE FOOL DIR
UI_DIR =  ROOT_DIR / "ui"
QSS_PATH = ROOT_DIR / "style" / "main.qss"

class MyWindow(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR/"merlins_lamp.ui", self)
        self.stackedWidget.setCurrentIndex(0)
        
        self.filter_type = None
        self.filter_prio = None
        self.filter_status = None
        
        self.adminAccess = False
        
        self.db = databaseManager()
        
        
        self.pushButton_userLogIn.clicked.connect(self.userLogIn)
        self.pushButton_AdminSignIn.clicked.connect(self.adminLogin)
        self.pushButton_register.clicked.connect(self.userRegister)
        
        self.btn_apply_filter.clicked.connect(self.apply_filter)
        self.pushButton_add_request.clicked.connect(self.add_request)
        self.comboBox_SortPriority.currentTextChanged.connect(self.filter_Priority)
        self.comboBox_SortStatus.currentTextChanged.connect(self.filter_Status)
        self.comboBox_SortRequest.currentTextChanged.connect(self.filter_RequestType    )
        
       
        
    def userRegister(self) -> bool:
        dialog = RegisterPage(self)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            return True
        
    def userLogIn(self) -> bool:
        self.username = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        if self.db.userLogin(self.username, self.password):
            print(f"welcome {self.username}")
            self.stackedWidget.setCurrentIndex(1)
            self.load_request()
            
            
            return True
        
        QMessageBox.warning(self, "Try again", "Wrong username or password")
        return False
    
    def adminLogin(self): 
        self.adminAccess = True
        self.userLogIn()
        
            
    def add_request(self):
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
            QMessageBox.information(self, "Empty Requests", "There is no requests in the database.")
            return False;
        
        requests_frame = self.frame_allRequests.layout()
        
        if self.adminAccess:
            for r in self.requests:
            
                widget = adminQFrame(r, self)
                requests_frame.addWidget(widget)
            return True
        else:
            for r in self.requests:
            
                widget = userQFrame(r, self)
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
        if newFiltered is None:
            QMessageBox.warning(self, "No Results", "There are no results with the applied filter.") 
        else:
            self.update_requests(newFiltered)  
            QMessageBox.information(self, "Applied filter", "Loading requested requests")
                      
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
        
    def filter_RequestType(self):
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