import pytest
import System


# Fails if professor tries to add a student to a course that they are not a professor of
def test_add_student(grading_system):
    username = 'saab'
    password = 'boomr345'
    grading_system.login(username, password)
    student = 'hdjsr7'
    course = 'databases'
    valid_courses = grading_system.users[username]['courses']
    assert course in valid_courses
    grading_system.usr.add_student(student, course)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
