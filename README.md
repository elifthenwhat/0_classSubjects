# Python Learning Notes

## Introduction
Hello, this is my lecture notes from *Python Crash Course*.  
The goal of these notes is to:  
- Store key information in one place  
- Provide quick reference for Python concepts  
- Include examples and testing practices  
- Serve as a study and revision tool  

## Table of Contents
* [Chapter 2: Variables and Simple Data Types](#chapter-2-variables-and-simple-data-types)
* [Chapter 3: Introducing Lists](#chapter-3-introducing-lists)
* [Chapter 4: Working with Lists](#chapter-4-working-with-lists)
* [Chapter 5: If Statements](#chapter-5-if-statements)
* [Chapter 6: Dictionaries](#chapter-6-dictionaries)
* [Chapter 7: User Input and While Loops](#chapter-7-user-input-and-while-loops)
* [Chapter 8: Functions](#chapter-8-functions)
* [Chapter 9: Classes](#chapter-9-classes)
* [Chapter 10: Files and Exceptions](#chapter-10-files-and-exceptions)
* [Chapter 11: Testing Your Code](#chapter-11-testing-your-code)

---

** Chapter 2: Variables and Simple Data Types
* Variables store data values.
* Basic types: int, float, str, bool.
* Example:
age = 25
name = "Alice"
height = 5.7
is_student = True

** Chapter 3: Introducing Lists
* Lists store multiple items.
* Use [] to create a list.
fruits = ["apple", "banana", "cherry"]

** Chapter 4: Working with Lists
* Access items by index: fruits[0]
* Modify, add (append), remove (del/pop)
* Loop through lists with for
for fruit in fruits:
    print(fruit)

** Chapter 5: If Statements
* Conditional logic: if, elif, else
if age >= 18:
    print("Adult")
else:
    print("Minor")

** Chapter 6: Dictionaries
* Store key-value pairs: {key: value}
* Access: dict[key], add/update: dict[new_key] = value
person = {"name": "Alice", "age": 25}
print(person["name"])

** Chapter 7: User Input and While Loops
* input() to get user input
* while loops repeat until condition is False
while True:
    msg = input("Enter message (q to quit): ")
    if msg == 'q':
        break
    print(msg)

** Chapter 8: Functions
* Reusable blocks of code with def
* Can return values
def greet(name):
    return f"Hello, {name}!"

** Chapter 9: Classes
* Classes define objects with attributes and methods
* __init__() initializes objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is sitting.")

** Chapter 10: Files and Exceptions
* Read/write files using open() with modes: 'r', 'w', 'a', 'r+'
* Handle errors with try/except
* Use with for safe file handling
with open("data.txt", "r") as file:
    content = file.read()

** Chapter 11: Testing Your Code
* Purpose: Ensure code works, catch errors early, allow safe changes
* Unit Tests: Verify a specific function’s behavior
* Test Case: Collection of unit tests
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

* Assert Methods: assertEqual, assertTrue, assertIn, assertFalse, etc.
* Failing Tests: Don’t change the test; fix the code
* Optional Parameters Example:
def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

* Testing Classes: Test methods and object behavior. Use setUp() for reusable objects
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    def store_response(self, new_response):
        self.responses.append(new_response)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        self.my_survey = AnonymousSurvey("What language did you first learn?")
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        for r in self.responses:
            self.my_survey.store_response(r)
        for r in self.responses:
            self.assertIn(r, self.my_survey.responses)

* Benefits: Confidence in code, prevents breaking functionality, easier collaboration