import pytest
from backend.database import databaseManager
from backend.Request import Request,Priority,StatusType
from frontend.RequestFrame import requestQFrame
from frontend.admin_user_request_template import userQFrame,adminQFrame
from datetime import datetime
from frontend.register_page import RegisterPage
from PyQt6.QtWidgets import QDialog


@pytest.fixture
def sample_requests():
    return Request("Title test", "Feature", Priority.LOW, StatusType.Unread, "Test content", datetime.now(), 1, 20, 20)

@pytest.fixture
def db_manager():
    return databaseManager()

def test_userQframe(qtbot, sample_requests):
    widget = userQFrame(sample_requests)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(3000)
    
def test_adminQframe(qtbot, sample_requests):
    widget = adminQFrame(sample_requests)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(3000)

def test_request_template_init(qtbot, sample_requests):
    widget = requestQFrame(sample_requests)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(3000)
    
    
    assert widget.label_date.text() == sample_requests.formatted_date
    assert widget.label_request_user.text() == "AJ"
    assert widget.label_requestID.text() == f'Request #{str(20)}'
    assert widget.label_request_title.text() == "Title test"
    assert widget.label_request_type.text() == "Feature"
    assert widget.label_content.text() == "Test content"
    assert widget.comboBox_AdminPriority.currentText() == sample_requests.priority.name
    assert widget.comboBox_AdminStatus.currentText() == sample_requests.status.name
    assert widget.upvote_label.text() == str(sample_requests.upvotes)
    
def test_AdminUpdatePrio(qtbot, sample_requests):
    widget = adminQFrame(sample_requests)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(10000)
    
    assert widget.comboBox_AdminPriority.currentText() == Priority.MEDIUM.name
    assert widget.comboBox_AdminStatus.currentText() == StatusType.Finished.name
    
    
    
def test_RegisterPage_init(qtbot):
    widget = RegisterPage()
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(5000)
    
def test_RegisterPage_register(qtbot):
    result = RegisterPage().exec()
    final = False
    
    
    assert result is QDialog.DialogCode.Accepted
    
    
def test_upvotes(qtbot, sample_requests):
    widget = requestQFrame(sample_requests)
    old = sample_requests.upvotes
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(10000)
    
    assert sample_requests.upvotes == old + 1
    