import pytest
from backend.database import databaseManager
from backend.Request import Request
from frontend.request_template import requestQFrame

def test_request_template_init(qtbot):
    request = Request("test 1", "Request type test", "Content test", "mm/dd/yy", "AJ test", "10")
    widget = requestQFrame(request)
    qtbot.addWidget(widget)
    widget.show()
    qtbot.wait(3000)
    
    assert widget.label_date.text() == "mm/dd/yy"
    assert widget.label_request_user.text() == "AJ test"
    assert widget.label_requestID.text() == "10"
    assert widget.label_request_title.text() == "test 1"
    assert widget.label_request_type.text() == "Request type test"
    assert widget.label_content.text() == "Content test"
