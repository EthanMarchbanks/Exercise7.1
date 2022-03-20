import pytest
import System


# Passes because it returns the correct grades
def test_check_grades(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    grades = grading_system.usr.check_grades('databases')
    grade_check = grading_system.users['akend3']['courses']['databases']['assignment1']['grade']
    assert grades[0][1] == grade_check


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
