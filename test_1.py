import pytest
import System


# Passes because correct name is set
def test_login(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(username, password)
    assert grading_system.usr.name == 'cmhbf5'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
