import pytest
import System


# Fails due to KeyError if the student is not in the class to be dropped from
def test_drop_student(grading_system):
    username = 'saab'
    password = 'boomr345'
    grading_system.login(username, password)
    student = 'yted91'
    grading_system.usr.drop_student(student, 'comp_sci')
    user_data = grading_system.users[student]['courses']
    assert 'comp_sci' not in user_data


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
