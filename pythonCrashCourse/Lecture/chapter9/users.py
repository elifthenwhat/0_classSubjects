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
        
class Privileges:
    """A simple attempt to model privileges for a user"""
    def __init__(self, privileges = ["Can add", "Can update", "Can delete"]):
        """Initialize the privileges attributes"""
        self.privileges = privileges 
        
    def show_privileges(self):
        print("These are the Administrator's privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")
        
class Administrator(User):
    """Represents an aspect of a User, specific to the adminsitrator"""
    def __init__(self, first_name, last_name, id_number, work_section):
        """
        Initialize attributes of the parent class
        Initilize attributes specific to the Adminsitrator 
        """
        super().__init__(first_name, last_name, id_number, work_section)
        self.privileges = Privileges()
        
