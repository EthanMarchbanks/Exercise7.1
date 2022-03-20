import pytest
import System


# Fails because it returns assignments for comp_sci, not the provided course
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    assignments = grading_system.usr.view_assignments('databases')
    assignments_ref = grading_system.courses['databases']['assignments']
    assignments_check = []
    for key in assignments_ref:
        assignments_check.append([key, assignments_ref[key]['due_date']])
    assert assignments == assignments_check


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
