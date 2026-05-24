from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QFrame
from backend.Request import Request, Priority, StatusType
from pathlib import Path
from backend.database import databaseManager
from frontend.RequestFrame import requestQFrame

CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent
BACK_DIR = SRC_DIR/"backend"
ROOT_DIR = SRC_DIR.parent
UI_DIR = ROOT_DIR / "ui"

class adminQFrame(requestQFrame):
    def __init__(self, request, parent=None):
        file_path = UI_DIR / "admin_request_template.ui"
        super().__init__(request, file_path, parent)
        
        self.comboBox_AdminPriority.blockSignals(True)
        self.comboBox_AdminStatus.blockSignals(True)
        
        if self.request.priority is not None:
            self.comboBox_AdminPriority.setCurrentIndex(self.request.priority.value)
            
                    
        #3EB489
        if self.request.status is not None:
            self.comboBox_AdminStatus.setCurrentIndex(self.request.status.value)
        
        
        self.comboBox_AdminPriority.blockSignals(False)
        self.comboBox_AdminStatus.blockSignals(False)
        
        self.comboBox_AdminPriority.currentTextChanged.connect(self.updatePriority)
        self.comboBox_AdminStatus.currentTextChanged.connect(self.updateStatus)
        self.updateColor()
        
    def updatePriority(self):
        try:
            newPrio = Priority[self.comboBox_AdminPriority.currentText()]
            self.request.priority = newPrio
            self.db.update_priority(self.request.requestID, newPrio)
            print(f"Object Updated: ID {self.request.requestID} is now {newPrio}")
            self.updateColor()
        
        except ValueError:
            print(f"Priority is not a valid Enum: {ValueError}")
            
    def updateStatus(self):
        try:
            newStatus = StatusType[self.comboBox_AdminStatus.currentText()]
            self.request.status = newStatus
            self.db.update_status(self.request.requestID, newStatus)
            print(f"Object Updated: ID {self.request.requestID} is now {newStatus}")
            self.updateColor()
        
        except ValueError:
            print(f"Status is not a valid Enum: {ValueError}")
            
    def updateColor(self):
        match self.request.priority.value:
                case 0: #undefined
                    self.comboBox_AdminPriority.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:grey;
                                                              """)
                case 1: #Low
                    self.comboBox_AdminPriority.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#72A0C1;
                                                              """)
                case 2: #medium
                    self.comboBox_AdminPriority.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#E9D66B;
                                                              """)
                case 3:#High
                    self.comboBox_AdminPriority.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#660000;
                                                              """)
                    
        match self.request.status.value:
                case 0: #Unread
                    self.comboBox_AdminStatus.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:grey;
                                                              """)
                case 1: #Working
                    self.comboBox_AdminStatus.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#72A0C1;
                                                              """)
                case 2: #Finished
                    self.comboBox_AdminStatus.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#E9D66B;
                                                              """)
                case 3:#High
                    self.comboBox_AdminStatus.setStyleSheet("""
                                                              border-radius: 16px;
                                                              background-color:#660000;
                                                              """)
        
        
class userQFrame(requestQFrame):
    def __init__(self, request, parent=None):
        file_path = UI_DIR / "user_request_template.ui"
        super().__init__(request, file_path, parent)
        self.priority_label.setText(self.request.priority.name)
        
        
        self.status_label.setText(self.request.status.name)
        self.updateColor()
        
    def updateColor(self):
        match self.request.priority.value:
                case 0: #undefined
                    self.priority_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:grey;
                                                              padding: 8px;
                                                              """)
                case 1: #Low
                    self.priority_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:#72A0C1;
                                                              padding: 8px;
                                                              """)
                case 2: #medium
                    self.priority_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:#E9D66B;
                                                              padding: 8px;
                                                              color: black;
                                                              """)
                case 3:#High
                    self.priority_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:#660000;
                                                              padding: 8px;
                                                              """)
                    
        match self.request.status.value:
                case 0: #Unread
                    self.status_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:grey;
                                                              padding: 8px;
                                                              """)
                case 1: #Working
                    self.status_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:#72A0C1;
                                                              padding: 8px;
                                                              """)
                case 2: #Finished
                    self.status_label.setStyleSheet("""
                                                              border-radius: 8px;
                                                              background-color:#3EB489;
                                                              padding: 8px;""")
                
        
        