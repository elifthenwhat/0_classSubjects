# Python Crash Course Notes

Hello, this is my lecture notes from Python Crash Course.  
The goal of these notes is to:  
- Have information stored for reference  
- Quickly find Python concepts  
- Help with exercises and review

## Table of Contents

2. Chapter 2: Variables and Simple Data Types  
3. Chapter 3: Introducing Lists  
4. Chapter 4: Working with Lists  
5. Chapter 5: If Statements  
6. Chapter 6: Dictionaries  
7. Chapter 7: User Input and While Loops  
8. Chapter 8: Functions  
9. Chapter 9: Classes  
10. Chapter 10: Files and Exceptions  
11. Chapter 11: Testing Your Code

---

## **Chapter 2: Variables and Simple Data Types**

* Variables store values like numbers, text, etc.  
* Use `=` to assign a value.  
* Common types: integers, floats, strings, booleans.  
* Operations include arithmetic, string concatenation, and boolean logic.  
* Constants: conventionally written in uppercase.  

---

## **Chapter 3: Introducing Lists**

* Lists store multiple items in a single variable.  
* Defined with square brackets `[]`.  
* Items can be of different types.  
* Access with index (starting at 0).  
* Basic operations: append, insert, remove, pop, sort, reverse.  

---

## **Chapter 4: Working with Lists**

* Looping through lists using `for`.  
* List comprehensions for compact code.  
* Slicing allows accessing portions of a list.  
* Copying lists requires slicing (`[:]`) to avoid reference issues.  
* Useful functions: `len()`, `min()`, `max()`, `sum()`.  

---

## **Chapter 5: If Statements**

* Conditional logic controls program flow.  
* Keywords: `if`, `elif`, `else`.  
* Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`.  
* Logical operators: `and`, `or`, `not`.  
* Nesting and combining conditions for complex logic.  

---

## **Chapter 6: Dictionaries**

* Store key-value pairs for fast lookup.  
* Defined with `{key: value}`.  
* Access, add, modify, and remove items.  
* Useful methods: `keys()`, `values()`, `items()`.  
* Loop through dictionary for processing data.  

---

## **Chapter 7: User Input and While Loops**

* `input()` reads input from the user.  
* Convert input to needed types (int, float, etc.).  
* `while` loops run until a condition is false.  
* Use `break` to exit early and `continue` to skip an iteration.  
* Useful for menus and repetitive prompts.  

---

## **Chapter 8: Functions**

* Functions encapsulate reusable logic.  
* Defined with `def function_name(parameters):`.  
* Return values with `return`.  
* Can have default, keyword, and arbitrary parameters.  
* Helps reduce code duplication and improves readability.  

---

## **Chapter 9: Classes**

* Classes represent objects with attributes and methods.  
* Defined with `class ClassName:`.  
* `__init__()` method initializes attributes.  
* Methods define behavior of the object.  
* Instances are created by calling the class.  
* Example usage: modeling real-world entities, organizing code.  

---

## **Chapter 10: Files and Exceptions**

* Files allow reading and writing data.  
* Open with `open(filename, mode)` and close with `close()` or use `with`.  
* Modes: `'r'` read, `'w'` write, `'a'` append.  
* Exception handling with `try-except` to prevent crashes.  
* Common exceptions: `FileNotFoundError`, `ZeroDivisionError`.  
* Helps programs handle errors gracefully.  

---

## **Chapter 11: Testing Your Code**

* Testing ensures code works as expected.  
* Use Python’s `unittest` module for automated tests.  
* **Unit tests** check one behavior; **Test cases** group multiple unit tests.  
* Use assert methods: `assertEqual`, `assertTrue`, `assertIn`, etc.  
* Failing tests indicate broken behavior—fix the code, not the test.  
* Optional parameters make functions flexible and maintain backward compatibility.  
* **Classes can be tested** like functions by checking method behavior.  
* Use `setUp()` in test cases to avoid repetitive setup.  
* Testing improves confidence, prevents bugs, and supports collaboration.  

---

**Best Practices**

* Test critical behaviors first.  
* Do not modify passing tests just to make new code work.  
* Always test after changes.  
* Keep tests clear, descriptive, and focused on one behavior.  
* Automated testing becomes essential as projects grow.  