# Chapter 7 - User Input and while Loops

"""
7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message say-
ing theyll have to wait for a table. Otherwise, report that their table is ready.
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
print("This is chapter 7.1")
rental_car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {rental_car}.")
print()

print("This is chapter 7.2")
guest_count = input("How many people are in the dinner group? ")
guest_count = int(guest_count)

if guest_count <= 0:
    print("You have no guest assigned for a table.")
elif guest_count <= 8:
    print(f"Please bring your {guest_count} guest to this table. ")
elif guest_count > 8:
    print(f"Sorry we do not have a table for {guest_count}.")
print()

"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying youll add that topping to their pizza.
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a persons age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
(continued)
User Input and while Loops 123
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)
"""
print("This is chapter 7.4")
pizza_toppings = []

topping = ""
while topping != "quit":
    topping = input("Please enter one topping\nenter 'quit' once complete (or no toppings needed): ")
    if topping == "quit":
        break
    elif topping != "quit":
        pizza_toppings.append(topping)

if len(pizza_toppings) <= 0:
    print("You have ordered no toppings on your pizza")
elif len(pizza_toppings) > 0:
    print("Creating your pizza now with the following toppings")
    for ingredients in pizza_toppings:
        print(ingredients)
print()

print("This is chapter 7.5")
age = ""
while age != "quit":
    age = input("Please enter your age\nPlease enter 'quit' to exit the program: ")
    if age == "quit":
        break
    elif age != "quit":    
        age = int(age)
        if age <= 0:
            print("Person does not exist.")
        elif age < 3:
            print("The ticket is $0.00 - FREE")
        elif age >= 3 and age < 12:
            print("The ticket is $10.00")
        elif age >= 12:
            print("The ticket is $15.00")
        print()
print()

print("This is chapter 7.6")

active = True

while active:
    age = input("Please enter your age\nEnter 'quit' to exit: ")
    if age == "quit":
        active = False
    else:
        age = int(age)
        if age <= 0:
            print("Person does not exist.")
        elif age < 2:
            print("Person is a baby")
        elif age < 5:
            print("Person is a toddler")
        elif age < 12:
            print("Person is a kid")
        elif age < 20:
            print("Person is a teen")
        else:
            print("Person is an adult")
print()

""" 

print("This is chapter 7.7")
Next code will cause infinite output: 
age = 1
while age <= 5:
    print(age)
    
"""

"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
7-10. Dream Vacation: Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""
print("This is chapter 7.8")
sandwich_orders = ["ham and cheese", "blt", "grilled cheese", "peanut butter"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print()

print("This is chapter 7.9")
sandwich_orders = ["pastrami","ham and cheese", "blt", "pastrami", "grilled cheese", "pastrami", "peanut butter"]

print("The deli has ran out of pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print()

print("This is chapter 7.10")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("What is your favorite food?")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? yes or no ")
    if repeat == "no":
        polling_active = False
        
print("\n-- Poll Results -- ")
for name, response in responses.items():
    print(f"{name.title()} likes {response}")