

class Employee:
    """A simple attempt to represent an Employee"""
    
    def __init__(self, first, last, annualSalary):
        self.first = first
        self.last = last
        self.annualSalary = annualSalary
        
    def give_raise(self, increase_raised = 5000):
        self.annualSalary = increase_raised
        return self.annualSalary