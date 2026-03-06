# This is chapter 8 - Functions
"""
8-1. Message: Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

print("This is chapter 8.1")

def display_message():
    print("This chapter is all about functions.")

display_message()
print()

print("This is chapter 8.2")

def favorite_book(title):
    print(f"One of my favorite bookes is {title}.")
    
favorite_book("Coraline")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""

print("This is chapter 8.3")
def make_shirt(size, text):
    print(f"You have orders a {size.upper()} shirt with the following text:")
    print(text)

make_shirt("large", "programming rules!")
print()

print("This is chapter 8.4")
def make_shirt(size = "LARGE", text = "I love Python!"):
    print(f"You have orders a {size.upper()} shirt with the following text:")
    print(text)
    print()
    
make_shirt()
make_shirt(size = "medium")
make_shirt(text = "I love Java!")
print()

print("This is chapter 8.5")
def describe_city(city, country = "USA"):
    print(f"{city.title()} is located in {country.title()}.")
    print()
    
describe_city("San Francisco")
describe_city("berlin", country= "Germany")
describe_city("Rome", "Italy")
print()

"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the albums dictionary. Make at least
one new function call that includes the number of songs on an album.
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an albums artist and title. Once you have that
information, call make_album() with the users input and print the dictionary
thats created. Be sure to include a quit value in the while loop.
"""
print("This is chapter 8.6")
def city_country(city, country):
    city_info = f"{city.title()}, {country.title()}"
    return city_info

print(city_country("san francisco", "america"))
print(city_country("las vegas", "america"))
print(city_country("rome", "italy"))
print()

print("This is chapter 8.7")
def make_album(artist, album, num_songs = None):
    artist_info = {"artist" : artist.title(), "album title" : album.title()}
    if num_songs:
        artist_info["number of songs"] = num_songs
    return artist_info

print(make_album("jimi hendrix", "psycadelic tunes"))
print(make_album("michael jackson", "thriller", 10))
print(make_album("bobby", "the bobby album", 6))
print()

print("This is chapter 8.8")
def make_album(artist, album, num_songs = None):
    artist_info = {"artist" : artist.title(), "album title" : album.title()}
    if num_songs:
        artist_info["number of songs"] = num_songs
    return artist_info

while True:
    print("\nPlease tell enter artist name:")
    print("(enter 'q' at anytime to quit)")
    
    artist_name = input("Enter artist name: ")
    if artist_name == 'q':
        break
    album_name = input("Enter album name: ")
    if album_name == 'q':
        break
    
    number_songs = input("Enter number of songs\nClick enter to leave number of songs out: ")
    if number_songs == 'q':
        break
    
    formatted_artist_info = make_album(artist_name, album_name, number_songs)
    print("The following artist info: ")
    print(formatted_artist_info)

print()
    
"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich thats being ordered. Call the function three times, using a different num-
ber of arguments each time.
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary thats returned to make sure all the information was
stored correctly.
"""
print("This is chapter 8.12")
def sandwich_builder(size, *toppings):
    print(f"\nYou have orders a {size.upper()} sandwich with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

sandwich_builder("large", "lettuce", "tomatoes", "pickels", "ham", "bacon")    
sandwich_builder("small", "peanut butter", "coco powder")
sandwich_builder("regular", "bacon", "letuce", "tomatoe")

print()

print("This is chapter 8.13")
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("Billy", "Cruz", location = "Canada", sport = "soccer", food = "pizza")
print("Information of user:")
print(user_profile)
print()

print("This is chapter 8.14")
def car_builder(manufacturer, model, **car_details):
    car_details["Manugacturer"] = manufacturer
    car_details["Model"] = model
    return car_details

car_profile = car_builder("Nissan", "Frontier", door_count = 4, enginer = "V6", radio = "touch screen")
print(car_profile)

"""
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""

print("This is chapter 8.15")
print("Please see files: printing_models.py and printing_functions.py")
print()

print("This is chapter 8.16")
print("Please see files: person_module.py and person_functions.py")
print()