print("This is an example of Inheritance - Chapter 9.6")
print()

class Restaurant:
    """A simple attempt to model a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}.")
        print(f"Home of the original {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is now open!")

class IceCream(Restaurant):
    """A simple attempt to model a Restaurant specific to an IceCream stand"""
    def __init__(self, restaurant_name, cuisine_type, flavors = []):
        """Initialize IceCream attributes"""
        super().__init__(restaurant_name, cuisine_type)
        """Connects restaurant_name and cuisine_type with the parent class"""
        self.flavors = flavors
        
johns_icecream = IceCream("John's Ice Cream", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
print("Let us describe the restaurant")
johns_icecream.describe_restaurant()
print()
print("Let us open the restaurant")
johns_icecream.open_restaurant()
print()

print(f"Let us print the flavors of {johns_icecream.restaurant_name}")
for i in johns_icecream.flavors:
    print(f"- {i}")
    
""" 
NOTE

Mutable default argument ⚠️ This is important:

def __init__(self, restaurant_name, cuisine_type, flavors = []):

Using a list as a default argument can cause bugs later. Best practice is:

def __init__(self, restaurant_name, cuisine_type, flavors=None):
    if flavors is None:
        flavors = []
"""   

print()
print()
print("This is an example of Inheritance - Chapter 9.7")
print()


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
        
class Admin(User):
    """A simple attempt to model a User specific to Admin"""
    def __init__(self, first_name, last_name, id_number, work_section, privileges = None):
        """Initialize the Admin's attributes"""
        super().__init__(first_name, last_name, id_number, work_section)
        """Connect the Admin attribute to the Admin class"""
        if privileges is None:
            self.privileges = ["Can add", "Can delete", "Can update"]
        else:
            self.privileges = privileges
            
    def show_privileges(self):
        print("These are the privileges an Admin user has: ")
        for i in self.privileges:
            print(f"- {i}")
            
dave_admin = Admin("dave", "sanchez", 2164, "IT")
dave_admin.show_privileges()
print()    
john_admin = Admin("john", "cruz", 3452, "human resource", ["Monitor traffic", "Scan history", "Grant access"])
john_admin.show_privileges()
print()

"""
NOTE

class Admin(User): 
    def __init__(self, first_name, last_name, id_number, work_section): 
        super().__init__(first_name, last_name, id_number, work_section) 
        self.privileges = ["Can add", "Cam delete", "Can update"]

Right now, every admin has the same privileges. You can make it more flexible:

class Admin(User):
    def __init__(self, first_name, last_name, id_number, work_section, privileges=None):
        super().__init__(first_name, last_name, id_number, work_section)
        if privileges is None:
            self.privileges = ["Can add post", "Can delete post", "Can ban user"]
        else:
            self.privileges = privileges

----------------------------

    def __init__(self, first_name, last_name, id_number, work_section, privileges = None):
        super().__init__(first_name, last_name, id_number, work_section)
        if privileges is None:
            self.privileges = ["Can add", "Can delete", "Can update"]
        else:
            self.privileges = privileges

It is NOT:
    def __init__(self, first_name, last_name, id_number, work_section, privileges = None):
        super().__init__(first_name, last_name, id_number, work_section)
    --> if self.privileges is None:
            self.privileges = ["Can add", "Can delete", "Can update"]
        else:
            self.privileges = privileges


self.privileges does not exist yet
Youre trying to check an attribute before youve created it, which will raise:
AttributeError: 'Admin' object has no attribute 'privileges'

You want to check the parameter privileges, not the attribute.
Remember:
- privileges → function argument
- self.privileges → instance attribute (created later)
"""
print()
print()
print("This is an example of inheritance + adding an instance as attributes")
print()

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
        
class Admin(User):
    """A simple attempt to model a User specific to Admin"""
    def __init__(self, first_name, last_name, id_number, work_section, privileges = None):
        """Initialize the Admin's attributes"""
        super().__init__(first_name, last_name, id_number, work_section)
        """Connect the Admin attribute to the Admin class"""
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self, privileges = None):
        self.privileges = privileges

        if privileges is None:
            self.privileges = ["Can add", "Can delete", "Can update"]
        else:
            self.privileges = privileges
            
    def show_privileges(self):
        print("These are the privileges an Admin user has: ")
        for i in self.privileges:
            print(f"- {i}")
            

dave_admin = Admin("dave", "sanchez", 2164, "IT")
dave_admin.privileges.show_privileges()
print()    
john_admin = Admin("john", "cruz", 3452, "human resource", ["Monitor traffic", "Scan history", "Grant access"])
john_admin.privileges.show_privileges()
print()


print()
print()
print("Add a method - Chapter 9.9")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The car has a {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size <= 75:
            return 260
        elif self.battery_size <= 100:
            return 315
        else:
            return 400

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

# Example
dave_car = ElectricCar("Tesla", "Model Y", 2022)

print("Range before upgrade:", dave_car.battery.get_range())
dave_car.battery.upgrade_battery()
print("Range after upgrade:", dave_car.battery.get_range())

        
dave_car = ElectricCar("Tesla", "Model Y", 2022)
print("Dave's current battery size is:")
print(dave_car.battery_size.battery_size)
print("Now let us upgrade the battery from 75 to 100")
dave_car.battery_size.upgrade_battery()
print("The new battery size is: ")
print(dave_car.battery_size.battery_size)