"""A set of classes that can be used to represent a User"""

class User:
    """A simple attempt to model a user"""
    def __init__(self, first_name, last_name, id_number, work_section):
        "Initialize first and last names"
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.work_station = work_section
        
    def describe_user(self):
        "Describe user information"
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"Badge Number: {self.id_number} Work Section: {self.work_station.title()}")
        
    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
        
