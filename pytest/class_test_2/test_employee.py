# Write a test file for Employee with two test functions, test_give_default 
# _raise() and test_give_custom_raise(). Write your tests once without using a 
# fixture, and make sure they both pass. Then write a fixture so you don’t have to 
# create a new employee instance in each test function. Run the tests again, and 
# make sure both tests still pass.
import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Create an Employee object for use in all test functions."""
    emp = Employee("Ram","Bahadur",10_000)
    return emp

def test_give_default_raise(employee):
    """Test that the default raise increases the employee's salary by 5000."""
    employee.give_raise()
    assert employee.annual_salary == 15_000, "Default raise did not work as expected."

def test_give_custom_raise(employee):
    """Test that a custom raise value correctly increases the employee's salary."""
    employee.give_raise(3_000)
    assert employee.annual_salary == 13_000, "Custom raise did not work as expected."