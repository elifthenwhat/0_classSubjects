# Python Crash Course

## Table of Contents
1. [Variables and Simple Data Types](#chapter-2-variables-and-simple-data-types)
2. [Introducing Lists](#chapter-3-introducing-lists)
3. [Working with Lists](#chapter-4-working-with-lists)
4. [If Statements](#chapter-5-if-statements)
5. [Dictionaries](#chapter-6-dictionaries)
6. [User Input and While Loops](#chapter-7-user-input-and-while-loops)
7. [Functions](#chapter-8-functions)
8. [Classes](#chapter-9-classes)
9. [Files and Exceptions](#chapter-10-files-and-exceptions)
10. [Testing Your Code](#chapter-11-testing-your-code)

---

## Chapter 2: Variables and Simple Data Types
* Variables store data.
* Types include integers, floats, strings, booleans.
* Use descriptive names and follow Python naming conventions.
* Simple operations: arithmetic, concatenation, and type conversion.

## Chapter 3: Introducing Lists
* Lists store multiple items in order.
* Use brackets `[]` to create lists.
* Access elements by index, starting at 0.
* Lists are mutable — you can change their elements.

## Chapter 4: Working with Lists
* Add elements: `append()`, `insert()`.
* Remove elements: `del`, `pop()`, `remove()`.
* Sort and reverse lists with `sort()` and `reverse()`.
* Loop through lists with `for` or `while`.

## Chapter 5: If Statements
* Conditional logic with `if`, `elif`, `else`.
* Use comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`.
* Combine conditions with `and`, `or`, `not`.
* Nested if statements for complex logic.

## Chapter 6: Dictionaries
* Dictionaries store key-value pairs: `{key: value}`.
* Access values with keys: `my_dict[key]`.
* Add/update: `my_dict[new_key] = value`.
* Remove: `del my_dict[key]`.
* Useful methods: `.keys()`, `.values()`, `.items()`.

## Chapter 7: User Input and While Loops
* Get user input: `input()` function.
* Convert input to desired type: `int(input())`, `float(input())`.
* While loops repeat as long as a condition is True.
* Use `break` and `continue` to control loops.

## Chapter 8: Functions
* Define functions with `def`.
* Use parameters and return values.
* Keep functions focused on a single task.
* Example:
```python
def greet_user(name):
    return f"Hello, {name.title()}!"


** Chapter 9: Classes
* Classes define objects with attributes and methods.
* Use __init__() to initialize objects.
* Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

** Chapter 10: Files and Exceptions
* Read/write files using open().
* Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write).
* Handle errors with try and except.
* Use with for safe file handling.

** Chapter 11: Testing Your Code
* Purpose: Ensure code works, catch errors early, allow safe changes.
* Unit Tests: Verify a specific function’s behavior.
* Test Case: Collection of unit tests.
