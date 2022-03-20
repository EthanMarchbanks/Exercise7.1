import pytest
import System


# Passes because only accepts correct password
def test_check_password(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    assert grading_system.check_password(username, password) == True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
