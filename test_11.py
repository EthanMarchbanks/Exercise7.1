import pytest
import System


# Fails because the password is case-sensitive, thus not setting the usr
def test_11(grading_system):
    username = 'cmhbf5'
    password = 'besTTA'
    grading_system.login(username, password)
    assert grading_system.usr.name == 'cmhbf5'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
