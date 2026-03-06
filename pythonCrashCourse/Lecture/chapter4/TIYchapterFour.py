"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
4-2. Animals: Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
"""

print("This is chapter 4.1")
pizzaList = ["pepperoni", "cheese", "sausage"]
for pizza in pizzaList:
    print(pizza)
print()

for pizza in pizzaList:
    print(f"I like {pizza} pizza.")
print()

for pizza in pizzaList:
    print(f"I LOVE {pizza.upper()} PIZZA!")
print("Gosh do I love pizza!")
print()

print("This is chapter 4.2")
animals = ["dog", "cat", "cow"]
for animal in animals:
    print(animal)
print()

for animal in animals:
    print(f"A {animal} would make a great pet!")
print()

for animal in animals:
    print(f"{animal.title()} would make a great pet.")
print("All of these animals can also live on a farm.")
print()


"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""

print("This is chapter 4.3")
for i in range(1,21):
    print(i)
print()

print("This is chapter 4.4")
"""
for i in range(1, 100000001):
    print(i)
    
This would take a while or the program would crash
"""
print()

print("This is chapter 4.5")
# To shorten the program run time, lets make it 100001
numbers = list(range(1,100001))
print(f"The minimum number of list is {min(numbers)}")
print(f"The maximum number of the list {max(numbers)}")
print()
# Lets print a list using the list function
moreNumbers = list(range(1,11))
print(moreNumbers)
print()

print("This is chapter 4.6")
oddNumbers = list(range(1,21,2))
for oddNumber in oddNumbers:
    print(oddNumber)
print()

print("This is chapter 4.7")
numThrees = list(range(3,31,3))
for numThree in numThrees:
    print(numThree)
print()

print("This is chapter 4.8")
cubes = []
for i in range(1,11):
    val = i ** 3
    cubes.append(val)
    
for cube in cubes:
    print(cube)
print()

print("This is chapter 4.9")
cubes = [value ** 3 for value in range(1,11)]
print(cubes)
print()

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that programs list.
• Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friends favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""
print("This is chapter 4.10")
sandwiches = ["ham and cheese", "tuna", "blt", "chicken", "veggie"]
print(f"This is the first three sandwiches on the menu: {sandwiches[0:2]}")
print()

print(f"This is the middle set of sandwiches: {sandwiches[1:4]}")
print()

print(f"This is the last three of sandwiches: {sandwiches[-3:]}")
print()

print("This is chapter 4.11")
pizzaList = ["pepperoni", "cheese", "sausage"]
friendList = pizzaList[:]

pizzaList.append("hawaiian")
friendList.append("vegetarian")
print("My favorite pizzas are:")
for pizza in pizzaList:
    print(pizza)
print()
print("My friend's favortie pizzas are:")
for pizza in friendList:
    print(pizza)
print()

print("This is chapter 4.12")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""
items = ("chicken", "steak", "pasta", "pizza", "salad")
print("Available food items:")
for item in items:
    print(item)
print()
"""
items[1] = "soup" -- program rejects changes to tuples
print(items)
"""
items = ("bread", "soup", "pasta", "pizza", "salad")
print("Updated menu food items:")
for item in items:
    print(item)
print()