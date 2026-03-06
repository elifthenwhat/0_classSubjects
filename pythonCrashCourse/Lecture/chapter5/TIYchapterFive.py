"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\ n Is car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.
5-2. More Conditional Tests: You dont have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
print("This is chapter 5.1")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print()
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print()

print("This is chapter 5.2")
pieQuant = 17
if pieQuant == 17:
    print(True)
if pieQuant != 17:
    print(False)
print()

car = "BMW"
print(car.lower() == "bmw")
car = "BMW"
print(car.lower() == "audi")
print()

numSeats = 80
audiencePop = 100
if audiencePop > numSeats:
    print("There is not enough seats")
if audiencePop <= numSeats:
    print("We have enough seats")
print()

colorOne = "green"
colorTwo = "red"
if colorOne == "green" and colorTwo == "red":
    print("The color combination is yellow")
print()

age = 21
if age >= 18 or age >= 21:
    print("You are old enough to vote")
print()

cars = ["BMW", "Audi", "Toyota"]
if "BMW" in cars:
    print(True)
print()
if "Nissan" not in cars:
    print(True)
print()

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the aliens color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the aliens color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the aliens color isnt green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
"""

print("This is chapter 5.3")
alien_color = "green"
if alien_color == "green":
    print("player earned 5 points")
if alien_color == "blue":
    print("Player earned a bonus point")
print()

print("This is chapter 5.4")
alien_color = "yellow"
if alien_color == "green":
    print("Player earned 5 points")
else:
    print("Player earned 10 points")
print()

alien_color = "yellow"
if alien_color == "yellow":
    print("Player earned 5 points")
else:
    print("Player earned 10 points")
print()

print("This is chapter 5.5")
alien_color = "red"
if alien_color == "green":
    print("Player earned 5 points")
elif alien_color == "yellow":
    print("Player earned 10 points")
else: 
    print("Player earned 15 points")
print()
alien_color = "yellow"
if alien_color == "green":
    print("Player earned 5 points")
elif alien_color == "yellow":
    print("Player earned 10 points")
else: 
    print("Player earned 15 points")
print()
alien_color = "green"
if alien_color == "green":
    print("Player earned 5 points")
elif alien_color == "yellow":
    print("Player earned 10 points")
else: 
    print("Player earned 15 points")
print()

print("This is chapter 5.6")
age = -3

if 0 < age < 2:
    print("That person is a baby")
elif 2 <= age < 4:
    print("That person is a toddler")
elif 4 <= age < 13:
    print("That person is a kid")
elif 13 <= age < 20:
    print("That person is a teen")
elif 20 <= age < 65:
    print("That person is an adult")
elif age >= 65:
    print("That person is an elder")
else:
    print("That person does not exist")
print()

print("This is chapter 5.7")
favorite_fruits = ["apple", "berry", "melon", "orange"]
if "banana" in favorite_fruits:
    print("You really like bananas")
if "cherry" in favorite_fruits:
    print("You really like cherries")
if "apple" in favorite_fruits:
    print("you really like apples")
if "melon" in favorite_fruits:
    print("You really like melons")
if "kiwi" in favorite_fruits:
    print("You really like kiwis")
print()

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, youll need to make a copy of
current_users containing the lowercase versions of all existing users.)
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""
print("This is chapter 5.8")
user_names = ["bbob245", "sruz245", "mago246", "aams247", "ctos248", "admin"]
for user in user_names:
    if user == "admin":
        print("Hello Admin")
    else:
        print(f"Hello {user.upper()}")
print()

print("This is chapter 5.9")
names = ["aams247", "ctos248", "admin"]
if names:   
    for name in names:
        if name == "admin":
            print("Hello Admin")
        else:
            print(f"Hello {name.upper()}")
else:
    print("We need to find some users!")
print()

names = []
if names:   
    for name in names:
        if name == "admin":
            print("Hello Admin")
        else:
            print(f"Hello {name.upper()}")
else:
    print("We need to find some users!")
print()

print("This is chapter 5.10")
current_users = ["sam", "bill", "dave", "karen", "john"]
new_users = ["Mike", "Brian", "Steve", "Karen", "John"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user} is already taken.")
        print()
    else:
        print(f"That username {new_user} is available.")
        print()
print()
        
print("This is chapter 5.11")
numbers = list(range(1,10))
for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    elif num == 4:
        print("4th")
    elif num == 5:
        print("5th")
    elif num == 6:
        print("6th")
    elif num == 7:
        print("7th")
    elif num == 8:
        print("8th")
    elif num == 9:
        print("9th")
    else:
        print("Error")
 
        