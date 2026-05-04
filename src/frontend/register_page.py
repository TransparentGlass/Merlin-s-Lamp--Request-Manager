from PyQt6.QtWidgets import QWidget, QDialog
from PyQt6 import uic
from pathlib import Path
from backend.database import databaseManager

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent.parent
UI_DIR = ROOT_DIR / "ui"
class RegisterPage(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        try:
            uic.loadUi(UI_DIR / "RegisterPage.ui", self)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return False
        
        self.resetOutputLabel()
        self.db = databaseManager()
        # self.input_username
        # self.input_password
        # self.input_confirmPassword
        
        self.btn_createAccount.clicked.connect(self.validateRegistration)
      
    def resetOutputLabel(self):
        self.label_outputPassword.setText("")
        self.label_outputConfirm.setText("")
        self.label_outputUsername.setText("")
          
    def validateRegistration(self):
        self.resetOutputLabel()
        username = self.input_username.text()
        password = self.input_password.text()
        confirm_pass = self.input_confirmPassword.text()
        
        if len(username.strip()) < 3:
            self.label_outputUsername.setText( "Input more than 3 characters.")
            return False
        
        if username.isalnum() is False:
            self.label_outputUsername.setText( "Only letters and numbers allowed")
            return False
        
        if self.db.fetch_user_id(username): #If none, good. If exist, return
            self.label_outputUsername.setText("Username already exists.")
            return False
        
        if len(password) < 5:
            self.label_outputPassword.setText( "Password must be greater than 5 characters.")
            return False
        
        if password != confirm_pass:
            self.label_outputConfirm.setText( "Password and confirmation does not match.")
            return False
        
        if self.db.userRegister(username, password):
            self.accept()
            return True
            
    
        
       