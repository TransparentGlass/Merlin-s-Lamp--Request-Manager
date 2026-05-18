from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QLayout, QMainWindow, QApplication, QWidget

from frontend.request_submission import RequestSubmission
from backend.Request import Request, Priority, StatusType
from backend.database import databaseManager
from frontend.request_template_small import request_small 

from PyQt6.QtCore import Qt, QMargins, QPoint, QRect, QSize
from PyQt6.QtWidgets import QApplication, QLayout, QPushButton, QSizePolicy, QWidget

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent #Current Directory SRC
ROOT_DIR = BASE_DIR.parent #THE FOOL DIR
UI_DIR =  ROOT_DIR / "ui"
QSS_PATH = ROOT_DIR / "style" / "main.qss"

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_DIR/"merlins_lamp_2.0.ui", self)
        self.db = databaseManager()
        self.load_request()
        

    def load_request(self, requests = None) -> bool:
        if requests:
            self.requests = requests
        else:
            self.requests = self.db.fetch_requests()
            
        if not self.requests:
            print("Request is empty or error")
            return False;
        
        flow = FlowLayout(self.collection_requests)
            
        for r in self.requests:
            widget = request_small(r, self)
            flow.addWidget(widget)
        return True
    
class FlowLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(QMargins(5, 5, 5, 5))

        self._item_list = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self._item_list.append(item)

    def count(self):
        return len(self._item_list)

    def itemAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self._item_list):
            return self._item_list.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientation(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._do_layout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self._do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self._item_list:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def _do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0
        spacing = self.spacing()

        for item in self._item_list:
            style = item.widget().style()
            layout_spacing_x = style.layoutSpacing(
                QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Horizontal
            )
            layout_spacing_y = style.layoutSpacing(
                QSizePolicy.ControlType.PushButton, QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Vertical
            )
            space_x = spacing + layout_spacing_x
            space_y = spacing + layout_spacing_y
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y() 
      
      

app = QApplication([])

with open(QSS_PATH, "r") as f:
    style = f.read()
    app.setStyleSheet(style)
    
window = MyWindow()
window.show()
app.exec()  
