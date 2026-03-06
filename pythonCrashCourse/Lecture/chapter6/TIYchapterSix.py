"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
6-2. Favorite Numbers: Use a dictionary to store peoples favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each persons name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, lets call it a glossary.
• Think of five programming words youve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\ n) to insert a blank line between each word-meaning
pair in your output.
"""
print("This is chapter 6.1")
friend_1 = {"first_name":"samantha", "last_name":"wilingberg", "age":23, "city":"san diego"}
print(friend_1["first_name"])
print(friend_1["last_name"])
print(friend_1["age"])
print(friend_1["city"])
print()

print("This is chapter 6.2")
favorite_number = {"samantha":13, "carol":7, "bobby":25, "beth":21, "mike":33}
for name, number in favorite_number.items():
    print(f"{name.title()} favorite number is {number}.")
print()

print("This is chapter 6.3")
glossary = {"loop":"performs the same action on every item in a list.", "variable":"stores a value", "string": "a sequence of characters", "float": "numbers with decimals", "comments": "used to explain code but not affect code"}
for term, definition in glossary.items():
    print(f"{term.upper()} : {definition}")
print()

"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionarys keys and values. When
youre sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
6-6. Polling: Use the code in favorite_languages.py (page 97).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have
"""

print("This is chapter 6.4")
glossary = {"loop":"performs the same action on every item in a list.", "variable":"stores a value", "string": "a sequence of characters", "float": "numbers with decimals", "comments": "used to explain code but not affect code", "constant":"a value that does not change", "whitespace": "spaces, tabs, new lines"}
for term, definition in glossary.items():
    print(f"{term.upper()} : {definition}")
print()

print("This is chapter 6.5")
river_info = {"nile":"eygpt", "amazon":"brazil", "mississippi": "usa"}
for river, country in river_info.items():
    print(f"The {river.title()} river runs through {country.title()}.")
print()
for river in river_info.keys():
    print(river.title())
print()
for country in river_info.values():
    print(country.title())
print()

print("This is chapter 6.6")
friend_list = ["sam", "jen", "pat", "edward"]

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in friend_list:
    if name in favorite_languages:
        print(f"{name.title()} thank you for taking the poll")
    elif name not in favorite_languages:
        print(f"{name.title()} please take the poll")

print()
print("continuation of chapter 6.6")
program_names = ["python", "c", "java", "javascript"]

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for program in program_names:
    if program in favorite_languages.values():
        print(f"{program} is listed in favorite languages")
    elif name not in favorite_languages:
        print(f"{program} was not listed in favorite languages")
print()

"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owners name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each persons name and their favorite places.
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each per-
sons name along with their favorite numbers.
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each citys dictionary should be something like
country, population, and fact. Print the name of each city and all of the infor-
mation you have stored about it.
6-12. Extensions: Were now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chan
"""
print("This is chapter 6.7 - Dictionaries in a List")

friend_1 = {"first_name":"samantha", "last_name":"wilingberg", "age":23, "city":"san diego"}
friend_2 = {"first_name":"mike", "last_name":"diego", "age":25, "city":"las vegas"}
friend_3 = {"first_name":"william", "last_name":"cruz", "age":27, "city":"tacoma"}

people = [friend_1, friend_2, friend_3]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} and lives in {person['city']}.")
print()

print("This is chapter 6.8 - Dictionaries in a List") 
pet_1 = {"name": "max", "type": "dog", "owner":"john"}
pet_2 = {"name": "goldie", "type": "fish", "owner":"sarah"}
pet_3 = {"name": "beau", "type": "cat", "owner":"billy"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pet Name : {pet['name'].title()}")
    print(f"Animal Type : {pet['type'].title()}")
    print(f"Owner Name : {pet['owner'].title()}")
    print()

print()

print("This is chapter 6.9 - Dictionary")
favorite_places = {"mike":"italy", "sam":"california", "carol":"spain"}
for person, place in favorite_places.items():
    print(f"{person.title()} favorite place is {place.title()}.")
print()

print("This is chapter 6.10 - Dictionary in Dictionary")
favorite_number = {"samantha":{13}, "carol":{7, 11}, "bobby":{25, 24, 77}, "beth":{21, 42}, "mike":{33}}

for name, number in favorite_number.items():
    print(f"{name.title()} favorite number is: ")
    for num in number:
        print(f"{num}")
    print()
print()

print("This is chapter 6.11 - Dictionary in Dictionary")
cities = {"san diego": {"population": 100, "temperature": "hot", "activities":"surfing"}, "las vegas":{"population": 500, "temperature": "super hot", "activities":"gambling"}, "seattle": {"population": 1000, "temperature": "cold", "activities":"drink coffee"}}

for city, facts in cities.items():
    print(f"The city of {city.title()}: ")
    print(f"Population : {facts['population']}")
    print(f"Temperature : {facts['temperature']}")
    print(f"Activities : {facts['activities']}")
    print()
print()

print("This is chapter 6.12 - List in Dictionary")
favorite_food = {"sam": ["pizza", "apples", "burgers"], "dave": ["pinapples"], "sarah": ["pizza", "sandwiches"], "steve": []}

for person, food in favorite_food.items():
    if len(food) == 0:
        print(f"{person.title()} didnt list any foods")
    elif len(food) == 1: 
        print(f"{person.title()} favortie food is:")
        for item in food:
            print(item)
    elif len(food) > 1:
        print(f"{person.title()} favorite foods are: ")
        for item in food:
            print(item)
    print()
print()
