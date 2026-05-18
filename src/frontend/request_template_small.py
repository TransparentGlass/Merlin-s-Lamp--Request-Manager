from PyQt6.QtWidgets import QFrame
from PyQt6 import uic   
from backend.Request import Request
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent
BACK_DIR = SRC_DIR/"backend"
ROOT_DIR = SRC_DIR.parent
UI_DIR = ROOT_DIR / "ui"

class request_small(QFrame):
    def __init__(self, request: Request, parent = None):
        super().__init__(parent)
        uic.loadUi(UI_DIR / "small_request.ui", self)
        self.status_label.setText(request.status.name)
        self.title_label.setText(request.title)
        self.request_label.setText(request.request_type)
        
