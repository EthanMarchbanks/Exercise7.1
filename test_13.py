import pytest
import System


# Fails if professor tries to create assignment for a course that he is not a professor of
def test_create_assignment(grading_system):
    username = 'saab'
    password = 'boomr345'
    grading_system.login(username, password)
    course = 'databases'
    valid_courses = grading_system.users[username]['courses']
    assert course in valid_courses
    grading_system.usr.create_assignment('assignment_test', '01/01/01', course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
