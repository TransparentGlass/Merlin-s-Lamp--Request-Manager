from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QApplication
from frontend.request_submission import RequestSubmission
from backend.Request import Request, Priority, StatusType
from backend.database import databaseManager
from frontend.request_template import requestQFrame 

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent #Current Directory SRC
ROOT_DIR = BASE_DIR.parent #THE FOOL DIR
UI_DIR =  ROOT_DIR / "ui"
QSS_PATH = ROOT_DIR / "style" / "main.qss"

class MyWindow(QMainWindow){
    def 
}