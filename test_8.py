import pytest
import System


# Fails because it should not return true
def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    assert not grading_system.usr.check_ontime('01/01/01', '01/01/00')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
