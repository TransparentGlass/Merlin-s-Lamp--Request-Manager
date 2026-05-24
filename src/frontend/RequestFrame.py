from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication, QFrame
from backend.Request import Request, Priority, StatusType
from pathlib import Path
from backend.database import databaseManager


CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent
BACK_DIR = SRC_DIR/"backend"
ROOT_DIR = SRC_DIR.parent
UI_DIR = ROOT_DIR / "ui"

class requestQFrame(QFrame):
    def __init__(self, request: Request, filepath, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi(filepath, self)
        
        self.upvoted = False
        
        self.db = databaseManager()
        self.request = request
        self.label_date.setText(request.formatted_date)
        self.label_request_user.setText(self.db.fetch_username(request.authorID))
        self.label_requestID.setText(f"Request #{str(request.requestID)}")
        self.label_request_title.setText(request.title)
        self.label_request_type.setText(request.request_type)
        self.label_content.setText(request.content)
        self.upvote_label.setText(str(request.upvotes))
        
        # self.comboBox_AdminPriority.blockSignals(True)
        # self.comboBox_AdminStatus.blockSignals(True)
        
        # if self.request.priority is not None:
        #     self.comboBox_AdminPriority.setCurrentIndex(self.request.priority.value)
        # else:
        #     index = -1
        
        # if self.request.status is not None:
        #     self.comboBox_AdminStatus.setCurrentIndex(self.request.status.value)
        # else:
        #     status_index = -1
        
        # self.comboBox_AdminPriority.blockSignals(False)
        # self.comboBox_AdminStatus.blockSignals(False)
        
        # self.comboBox_AdminPriority.currentTextChanged.connect(self.updatePriority)
        # self.comboBox_AdminStatus.currentTextChanged.connect(self.updateStatus)
        self.pushButton_upvote.clicked.connect(self.upvote)
        
    
            
    def upvote(self):
        #if upvote false, upvote, else unupvote. Save it locally first and then save
        if self.upvoted:
            self.db.undoVote(self.request.requestID)
            self.upvoted = False
            self.request.upvotes -= 1
            self.upvote_label.setText(str(self.request.upvotes))
            return
        
        self.db.upvote(self.request.requestID)
        self.upvoted = True
        self.request.upvotes += 1
        self.upvote_label.setText(str(self.request.upvotes))
        return
        
        #update
        
        
        
        
        
        
        
        
        

        
        
        
        