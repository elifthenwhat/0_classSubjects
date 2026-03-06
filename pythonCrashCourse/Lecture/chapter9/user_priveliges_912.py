"""A set of classes that can be used to represent a User specifically an Administrator"""

from user_912 import User

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
        
