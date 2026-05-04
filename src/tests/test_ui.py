import pytest
from backend.database import databaseManager
from backend.Request import Request,Priority,StatusType
from frontend.request_template import requestQFrame
from datetime import datetime
from frontend.register_page import RegisterPage
from PyQt6.QtWidgets import QDialog


@pytest.fixture
def sample_requests():
    return Request("Title test", "Feature", Priority.LOW, StatusType.ONGOING, "Test content", datetime.now(), "AJ", 20)

@pytest.fixture
def db_manager():
    return databaseManager()

def test_request_template_init(qtbot, sample_requests):
    widget = requestQFrame(sample_requests)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(3000)
    
    
    assert widget.label_date.text() == sample_requests.formatted_date
    assert widget.label_request_user.text() == "AJ"
    assert widget.label_requestID.text() == str(20)
    assert widget.label_request_title.text() == "Title test"
    assert widget.label_request_type.text() == "Feature"
    assert widget.label_content.text() == "Test content"
    assert widget.comboBox_AdminPriority.currentText() == sample_requests.priority.value
    assert widget.comboBox_AdminStatus.currentText() == sample_requests.status.value
    
def test_request_template_updatePrio(qtbot, sample_requests, db_manager):
    widget = requestQFrame(sample_requests,)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(10000)
    
    assert widget.comboBox_AdminPriority.currentText() == Priority.MEDIUM.value
    assert widget.comboBox_AdminStatus.currentText() == StatusType.FINISHED.value
    
    
    
def test_RegisterPage_init(qtbot):
    widget = RegisterPage()
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(5000)
    
def test_RegisterPage_register(qtbot):
    result = RegisterPage().exec()
    final = False
    
    
    assert result is QDialog.DialogCode.Accepted
    

