import pytest
from backend.database import databaseManager
from backend.Request import Request, Priority, StatusType
from frontend.request_template import requestQFrame
from datetime import datetime

@pytest.fixture
def sample_requests():
    return Request("Title test", "Feature", Priority.LOW, StatusType.ONGOING, "Test content", datetime.now(), "AJ", 20)

@pytest.fixture
def db_manager():
    return databaseManager()

@pytest.fixture
def user():
    return {"username": "Klein", "password": "12345"}

def test_fetch_request(sample_requests):
    db = databaseManager()
    result = db.fetch_requests()
    
    assert result is None
    
def test_priority_update_cycle(db_manager):
    # Arrange
    req_id = 20
    new_priority = Priority.HIGH
    
    # Act
    success = db_manager.update_priority(req_id, new_priority)
    
    # Assert
    assert success is True
    
    # # Re-fetch to ensure it stuck
    # updated_reqs = db_manager.fetch_requests()
    # # Find our specific request in the list
    
    # req = next(r for r in updated_reqs if r.requestID == req_id)
    # assert req.priority == Priority.HIGH
    
def test_status_update_cycle(db_manager):
    # Arrange
    req_id = 20
    new_status = StatusType.FINISHED
    
    # Act
    success = db_manager.update_priority(req_id, new_status)
    
    # Assert
    assert success is True
    
def test_userSignIn(user, db_manager):
    username = user["username"]
    password = user["password"]
    
    success = db_manager.userRegister(username, password)
    
    assert success is True
    
def test_userSigninFail(user, db_manager):
    username = user["username"]
    password = "wrong password"
    success = db_manager.userRegister(username, password)
    
    assert success is False
    
def test_userLogin(user, db_manager):
    username = user["username"]
    password = user["password"]
    
    success = db_manager.userLogin(username, password)
    
    assert success is True
    
def test_userLogin_wrongPW(user, db_manager):
    
    username = user["username"]
    password = "1000000"
    
    success = db_manager.userLogin(username, password)
    
    assert success is False
    


