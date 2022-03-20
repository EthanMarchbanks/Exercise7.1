import pytest
import System


# Passes because it submits the assignment correctly and changes the db
def test_submit_assignment(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    grading_system.usr.submit_assignment('databases', 'assignment1', 'submission', '01/01/01')
    user_data = grading_system.users[grading_system.usr.name]['courses']['databases']
    assert 'assignment1' in user_data
    assert user_data['assignment1']['grade'] == 'N/A'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
