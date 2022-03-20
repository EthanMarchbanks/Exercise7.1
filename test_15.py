import pytest
import System
from datetime import datetime


# Fails if student tries to submit an assignment after the due date
def test_submit_assignment(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    course = 'comp_sci'
    duedate = datetime.strptime(grading_system.courses[course]['assignments']['assignment1']['due_date'], '%m/%d/%y')
    currentdate = datetime.now()
    assert not currentdate > duedate
    grading_system.usr.submit_assignment(course, 'assignment1', 'submission', '01/01/01')


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
