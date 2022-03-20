import pytest
import System


# Fails because changes grade to 0, not entered grade
def test_change_grade(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(username, password)
    grading_system.usr.change_grade("akend3", "comp_sci", "assignment1", 91)
    user_data = grading_system.users['akend3']['courses']['comp_sci']["assignment1"]
    assert user_data['grade'] == 91


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
