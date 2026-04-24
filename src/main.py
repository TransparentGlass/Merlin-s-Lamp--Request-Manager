from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from load_font import load_font

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src\merlins_lamp.ui", self)
        
        
        
        
        
# load_font()
app = QApplication([])

with open("style\main.qss", "r") as f:
    style = f.read()
    app.setStyleSheet(style)
    
window = MyWindow()
window.show()
app.exec()