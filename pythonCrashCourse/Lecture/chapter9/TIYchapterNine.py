from random import randint, choice

# This is chapter 9 - Classes

"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the users information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

print("This is chapter 9.1")

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
        

jimmy_johns = Restaurant("jimmy johns", "sub sandwiches")
print(jimmy_johns.restaurant_name)
print(jimmy_johns.cuisine_type)
print()

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()
print()

print("This is chapter 9.2")
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

pizza_hut = Restaurant("pizza hut", "pizza")
island_grub = Restaurant("island grub", "island food")
winchells_donuts = Restaurant("winchells", "donuts")

pizza_hut.describe_restaurant()
pizza_hut.open_restaurant()
print()

island_grub.describe_restaurant()
island_grub.open_restaurant()
print()

winchells_donuts.describe_restaurant()
winchells_donuts.open_restaurant()
print()


print("This is chapter 9.3")

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
        
tammy = User("tammy", "cruz", 1345, "human resource")
john = User("john", "santiago", 1424, "information technology")
bill = User("bill", "brown", "2446", "accounting")
sam = User("sam", "wise", 9582, "marketing")
    
    
tammy.describe_user()
tammy.greet_user()
print()
john.describe_user()
john.greet_user()
print()
bill.describe_user()
bill.greet_user()
print()
sam.describe_user()
sam.greet_user()
print()


"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers whove been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

print("This is chapter 9.4")

print("Chapter 9.4 part 1")
class Restaurant:
    """A simple attempt to model a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}.")
        print(f"Home of the original {self.cuisine_type}.")
        print(f"We are please to say we have served {self.number_served}")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is now open!")

print("Print the number initial amount of customer served")
jimmy_johns = Restaurant("jimmy johns", "sub sandwiches")
print(jimmy_johns.restaurant_name)
print(jimmy_johns.cuisine_type)
print(jimmy_johns.number_served)
print()

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()

print()
print("Print the updated amount of customers served")
jimmy_johns.number_served = 25

print(jimmy_johns.restaurant_name)
print(jimmy_johns.cuisine_type)
print(jimmy_johns.number_served)
print()

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()

print()
print("Add a method called set_number_served() to set number of customers served.")

class Restaurant:
    """A simple attempt to model a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}.")
        print(f"Home of the original {self.cuisine_type}.")
        print(f"We are please to say we have served {self.number_served}")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is now open!")
        
    def set_number_served(self, customer_count):
        """Set the number_served to the given value of customer_count"""
        self.number_served = customer_count
        

print("Print the number initial amount of customer served")
jimmy_johns = Restaurant("jimmy johns", "sub sandwiches")
print(jimmy_johns.restaurant_name)
print(jimmy_johns.cuisine_type)
print(jimmy_johns.number_served)
print()

jimmy_johns.set_number_served(100)

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()
print()

print("Print the increment value of customers served")

class Restaurant:
    """A simple attempt to model a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}.")
        print(f"Home of the original {self.cuisine_type}.")
        print(f"We are please to say we have served {self.number_served}")
        
    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is now open!")
        
    def set_number_served(self, customer_count):
        """Set the number_served to the given value of customer_count"""
        self.number_served = customer_count
        
    def increment_customerCount(self, increment_value):
        """Add the given amount to the increment value"""
        self.number_served += increment_value

jimmy_johns = Restaurant("jimmy johns", "sub sandwiches")
print(jimmy_johns.restaurant_name)
print(jimmy_johns.cuisine_type)
print(jimmy_johns.number_served)
print()

jimmy_johns.set_number_served(100)

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()

print()
jimmy_johns.increment_customerCount(50)

jimmy_johns.describe_restaurant()
jimmy_johns.open_restaurant()
print()

print("This is chapter 9.5")


class User:
    """A simple attempt to model a user"""
    def __init__(self, first_name, last_name, id_number, work_section, login_attempts = 0):
        "Initialize first and last names"
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.work_station = work_section
        self.login_attempts = login_attempts
        
    def describe_user(self):
        "Describe user information"
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"Badge Number: {self.id_number} Work Section: {self.work_station.title()}")
        
    def greet_user(self):
        """Greet user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
        
    def increment_login_attempts(self):
        """Increments the value of login attempts"""
        self.login_attempts += 1
        print(f"The current login attempt is: {self.login_attempts}")
    
    def reset_login_attempts(self):
        """Reset the login attempt count"""
        self.login_attempts = 0 
        print("You have reset your login attempts")
        print(f"Current login attempt count: {self.login_attempts}")
        
        
john = User("john", "cruz", 1446, "human resource")

john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print()
john.reset_login_attempts()
print()

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrators set of
privileges. Create an instance of Admin, and call your method.
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

print("This is chapter 9.6")


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

class IceCreamStand(Restaurant):
    """Represents a restaurant that is an Ice Cream Stand"""
    
    def __init__(self, restaurant_name, flavors=None, cuisine_type="ice cream"):
        """Initialize attributes of parent class and flavors"""
        super().__init__(restaurant_name, cuisine_type)
        if flavors is None:
            self.flavors = ["vanilla", "chocolate", "strawberry"]
        else:
            self.flavors = flavors

    def display_flavors(self):
        print(f"{self.restaurant_name.title()} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

JoeIceCream = IceCreamStand("Joes Ice Cream")
JoeIceCream.display_flavors()
print()

BobIceCream = IceCreamStand("Bobs Ice Cream", ["cookies & cream", "strawberry shortcake", "rockie road"])
BobIceCream.display_flavors()
print()


print("This is chapter 9.7")

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
        
class Administrator(User):
    """Represents an aspect of an User, specific to an Administrator"""
    def __init__(self, first_name, last_name, id_number, work_section, privileges = ["Can add post", "Can delete post", "Can ban user"]):
        "Initialize attributes of parent class, User"
        super().__init__(first_name, last_name, id_number, work_section)
        self.privileges = privileges 
        
    def show_privileges(self):
        print("These are the Administrator's privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")
        
Admin = Administrator("John", "Black", 2345, "IT")
Admin.show_privileges()
print()

print("This is chapter 9.8")

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
        
david_cruz = Administrator("david", "cruz", 4256, "human resource")
david_cruz.privileges.show_privileges()
print()

print("This is chapter 9.9")

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        """Check the battery size and set the capacity to 100"""
        if self.battery_size == 100:
            print("Battery size is 100")
        else:
            self.battery_size = 100
            print("The battery size was updated to 100")
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print()

my_prius = ElectricCar("toyota", "prius", 2020)
print(my_prius.get_descriptive_name())
my_prius.battery.get_range()
my_prius.battery.upgrade_battery()
my_prius.battery.get_range()

print()

"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
ule. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurants methods to show that the import statement is work-
ing properly.
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

print("Chapter 9.10 - Open restaurants.py and my_restaurants.py")
print()

print("Chapter 9.11 - Open users.py and my_user.py")
print()

print("Chapter 9.12 - Open users_912.py, user_priveliges_912.py, and my_user_912.py")
print()


print("This is chapter 9.13 - Import is on top of the file")

class Dice:
    """A simple attempt to model a dice"""
    def __init__(self, dice = 6):
        """Initialize dice attributes"""
        self.dice = dice 
        
    def roll_die(self):
        num_side = self.dice
        print(f"The dice has landed on {randint(1, num_side)}")
        
roll_1 = Dice()
roll_1.roll_die()
roll_2 = Dice()
roll_2.roll_die()
roll_3 = Dice()
roll_3.roll_die()
print()

print("This is a 10 sided die")
roll_4 = Dice(10)
roll_4.roll_die()
print()
print("This is a 20 side die")
roll_5 = Dice(20)
roll_5.roll_die()
print()

print("This is chapter 9.14")
characters = [1,2,3,4,5,6,7,8,9,10,"a", "b", "c", "d", "e"]
winning_ticket = []

i = 1
while i <= 4:
    winning_ticket.append(choice(characters))
    i = i + 1 

print("The winning ticket combination is:")
print(winning_ticket)
print()

print("This is chapter 9.15")
""" This will cause the program to run for a long time ... (lets put it in comments)
characters = [1,2,3,4,5,6,7,8,9,10,"a", "b", "c", "d", "e"]
my_ticket = ["b", 3, 6, "e"]

count = 0
winning_ticket = []

while my_ticket != winning_ticket:
    winning_ticket.append(choice(characters))
    count += 1
    
print(f"It took {count} tries to win the lottery.")
"""

    
