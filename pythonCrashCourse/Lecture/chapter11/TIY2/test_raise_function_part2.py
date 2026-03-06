import unittest
from raise_function import Employee

class TestEmployeeClass(unittest.TestCase):
    """Test for the Employee class"""
    
    def setUp(self):
        """
        Create an employee instance
        """
        self.employeeOne = Employee("Mike", "Santiago", 2000)
        
    def test_give_default_raise(self):
        employee_default_raise = self.employeeOne.give_raise()
        print(f"The employee raise is ${employee_default_raise}")
        print("\n")
        
    def test_give_custom_raise(self):
        employee_custom_raise = self.employeeOne.give_raise(3000)
        print(f"The employee raise is ${employee_custom_raise}")
        print("\n")
            
if __name__ == "__main__":
    unittest.main() 