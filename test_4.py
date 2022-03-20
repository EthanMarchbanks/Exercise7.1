import pytest
import System


# Passes because assignment is added to courses db
def test_create_assignment(grading_system):
    username = 'saab'
    password = 'boomr345'
    grading_system.login(username, password)
    grading_system.usr.create_assignment('assignment_test', '01/01/01', 'comp_sci')
    course_data = grading_system.courses['comp_sci']['assignments']
    assert 'assignment_test' in course_data


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
