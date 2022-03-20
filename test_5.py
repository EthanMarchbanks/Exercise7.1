import pytest
import System


# Fails because add_student function has an error in it?
def test_add_student(grading_system):
    username = 'saab'
    password = 'boomr345'
    grading_system.login(username, password)
    student = 'hdjsr7'
    grading_system.usr.add_student(student, 'comp_sci')
    user_data = grading_system.users[student]['courses']
    assert 'comp_sci' in user_data


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
