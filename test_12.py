import pytest
import System


# Fails if TA tries to change grade of a student in a course that he is not a TA of
def test_change_grade(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(username, password)
    course = 'comp_sci'
    valid_courses = grading_system.users[username]['courses']
    assert course in valid_courses
    grading_system.usr.change_grade("akend3", course, "assignment1", 91)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
