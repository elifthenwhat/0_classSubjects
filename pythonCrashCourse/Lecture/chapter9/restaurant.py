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

