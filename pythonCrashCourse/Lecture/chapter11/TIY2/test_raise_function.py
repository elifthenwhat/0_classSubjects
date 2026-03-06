import unittest
from raise_function import Employee

class TestEmployeeClass(unittest.TestCase):
    """Test for the Employee class"""
    
    def test_give_default_raise(self):
        employeeOne = Employee("Mike", "Santiago", 2000)
        employee_default_raise = employeeOne.give_raise()
        print(f"The employee raise is ${employee_default_raise}")
        print("\n")
        
    def test_give_custom_raise(self):
        employeeOne = Employee("Mike", "Santiago", 2000)
        employee_custom_raise = employeeOne.give_raise(3000)
        print(f"The employee raise is ${employee_custom_raise}")
        print("\n")
        
        
if __name__ == "__main__":
    unittest.main()