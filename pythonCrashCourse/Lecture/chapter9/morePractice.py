print("This is a simple class example using student")
print()
print()
class Student:
    """A simple attempt to model a student"""
    def __init__(self, name, grade):
        """"Initialize atttributes: name and grade"""
        self.name = name
        self.grade = grade 
        
    def relax(self):
        """Tell the student to take a break"""
        print(f"{self.name} it is lunch time, take a break.")
        
    def study(self):
        """Tell student to go back to work"""
        print(f"{self.name} break has ended. Go back to your studies")
        

johnny = Student("Johnny", "7th")
sammy = Student("Sammy", "9th")

print()

print(f"{johnny.name} is in {johnny.grade} grade.")
johnny.relax()
johnny.study()
print()

print(f"{sammy.name} is int the {sammy.grade} grade")
sammy.relax()
sammy.study()
print()


print()
print()
print("The following example is an example of Inheritance")
print()
print()

class Car:
    """This is a simple attempt to model a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer = 0
    
    def get_descriptive_name(self):
        descriptive_name = f"This is the {self.year} {self.make.upper()} {self.model.upper()} with {self.odometer} miles."
        return descriptive_name
        
    def update_odometer(self, miles):
        if miles < 0:
            print("The odometer cannot be a negative value.")
        elif miles < self.odometer:
            print("You cannot reverse miles")
        elif miles > self.odometer:
            self.odometer = miles
            print("Updating odomter ...")
            print(f"The odomter is updated to the current mileage: {miles}")
    
    def increment_odometer(self, miles):
        if miles < 0:
            print("You cannot increment mileage with a negative value.")
        else:        
            print(f"The current mileage is: {self.odometer}")
            self.odometer += miles
            print("Updating odomter ...")
            print(f"The odometer has incremented by {miles} miles and the current car mileage is {self.odometer}.")
            
    def fill_gas_tank(self):
        print("Currently filling gast tank ...")
        print("Gas tank is filled.")
        
 
class ElectricCar(Car):
    """A simple attempt to model an electric car with parent class 'Car' attribute & methods""" 
    def __init__(self, make, model, year): # Overide the __init__() method of the Car class
        """ Initialize attributes and methods of parent class 'Car' """
        super().__init__(make, model, year) 
        # Calls the Car class __init__ method and passing the ElectriCar make, model, year into it
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"The car has a {self.battery_size}-kwh battery")
        
    def fill_gas_tank(self):
        """Electric cars dont have a gas tank"""
        print("This car doesnt need a gas tank!")

        
my_car = Car("toyota", "tacoma", 2020)
my_car.fill_gas_tank() 
 
my_tesla = ElectricCar("Tesla", "model s", 2020)
my_tesla.fill_gas_tank()
 

""" 
my_car = Car("nissan", "gtr", 2020)
print("First let us print the specs:")
print(my_car.get_descriptive_name())
print()
print(f"Car Manufacturer: {my_car.make.upper()}")
print(f"Car Model: {my_car.model.upper()}")        
print(f"Car Year: {my_car.year}")
print(f"Current Mileage: {my_car.odometer}")
print()
print("Let us update the car mileage by 250 miles")
my_car.update_odometer(250)
print()
print("Let us increment the mileage after 1 year of use by 150 miles")
my_car.increment_odometer(150)
print()

print("Let us test a negative value for 'update_miilage'")
print(f"Current Mileage: {my_car.odometer} of -100")
my_car.update_odometer(-100)
print(f"Current Mileage: {my_car.odometer}")
print()
print("Let us test a value less than current mileage with 100")
print(f"Current Mileage: {my_car.odometer}")
my_car.update_odometer(100)
print(f"Current Mileage: {my_car.odometer}")
print("Let us increment the mileage by 100 again")
my_car.increment_odometer(100)
"""


# Instances as Attributes 
"""
For example, if we continue adding detail to the ElectricCar class, we might notice that were adding 
many attributes and methods specific to the cars battery. When we see this happening, we can stop and 
move those attributes and methods to a separate class called Battery. Then we can use a
Battery instance as an attribute in the ElectricCar class:
"""
print()
print()
print("Instances as Attributes")
print()
print()

class Car:
    """This is a simple attempt to model a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer = 0
        self.battery_size = Battery()
    
    def get_descriptive_name(self):
        descriptive_name = f"This is the {self.year} {self.make.upper()} {self.model.upper()} with {self.odometer} miles."
        return descriptive_name
        
    def update_odometer(self, miles):
        if miles < 0:
            print("The odometer cannot be a negative value.")
        elif miles < self.odometer:
            print("You cannot reverse miles")
        elif miles > self.odometer:
            self.odometer = miles
            print("Updating odomter ...")
            print(f"The odomter is updated to the current mileage: {miles}")
    
    def increment_odometer(self, miles):
        if miles < 0:
            print("You cannot increment mileage with a negative value.")
        else:        
            print(f"The current mileage is: {self.odometer}")
            self.odometer += miles
            print("Updating odomter ...")
            print(f"The odometer has incremented by {miles} miles and the current car mileage is {self.odometer}.")
            
    def fill_gas_tank(self, gas = 0):
        if gas == 0:
            print("You did not enter the amount of gas")
        elif gas <= 1:
            print("You poured 1 gallon of gas, that would be $10")
        elif gas <= 2:
            print("You have poured 2 gallons of gas, that would be $20")
        elif gas <= 3:
            print("You have poured 3 gallons of gas, that would be $30")
        
class Battery:
    """A simple attempt to model a battery for an electric car"""
    
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"The car has a {self.battery_size}-kwh battery")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        return range 
 
class ElectricCar(Car):
    """A simple attempt to model an electric car with parent class 'Car' attribute & methods""" 
    def __init__(self, make, model, year): # Overide the __init__() method of the Car class
        """ Initialize attributes and methods of parent class 'Car' """
        # Calls the Car class __init__ method and passing the ElectriCar make, model, year into it
        super().__init__(make, model, year) 
        self.battery_size = Battery()

    def fill_gas_tank(self):
        """Electric cars dont have a gas tank"""
        print("This car doesnt need a gas tank!")
        

dave_car = ElectricCar("Tesla", "Model S", 2020)
print("Lets print the description of Dave's car")
print(dave_car.get_descriptive_name())
print()
print("Let us update the odometer to 1000")
dave_car.update_odometer(1000)
print()
print("Let us increase the odometer to 2500")
dave_car.increment_odometer(2500)
print()
print("Let us see if we try to fill the gas tank")
dave_car.fill_gas_tank()
print()
print("Let us describe the battery")
dave_car.battery_size.describe_battery()
print()
print("Let us update the battery to 100 instead of 75")
dave_car.battery_size = Battery(100)
dave_car.battery_size.describe_battery()

print()
print()
print("Curious and Curios... lets try using the Battery class within the Car class")
print()
print()

john_F150 = Car("Ford", "F150", 2025)
print("Lets print the description of John's car")
print(john_F150.get_descriptive_name())
print()
print("Let us update the odometer to 1000")
john_F150.update_odometer(1000)
print()
print("Let us increase the odometer to 2500")
john_F150.increment_odometer(2500)
print()
print("Let us see if we try to fill the gas tank with 0 gallons")
john_F150.fill_gas_tank()
print("Let us see if we try to fill the gas tank with 3 gallons")
john_F150.fill_gas_tank(3)
print()
print("Let us describe the battery")
john_F150.battery_size.describe_battery()
print()
print("Let us update the battery to 100 instead of 75")
john_F150.battery_size = Battery(100)
john_F150.battery_size.describe_battery()