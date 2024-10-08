import pytest
from employee import Employee
#test given a raise to an employee using fixture
@pytest.fixture

def employee():
    #employee that will be available to all the test functions
    employee = Employee('Bryan','Vivanco',1_500)
    return employee

def test_give_default_raise(employee):
    giving_raise = employee.give_raise()
    assert giving_raise == 6_500       
    
def test_give_custom_raise(employee):
    giving_raise = employee.give_raise(7_000)
    assert giving_raise == 8_500   