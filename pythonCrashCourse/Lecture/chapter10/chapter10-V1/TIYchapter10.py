"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what youve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by stor-
ing the lines in a list and then working with them outside the with block.
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Heres a quick example showing how to replace
'dog' with 'cat' in a sentence:
>> message = "I really like dogs."
>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

print("This is chapter 10.1")
print()
print("This is chapter 10.1 part 1 - READING THE ENTIRE FILE")
print()
filename = "learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
print(contents)
print()


print("This is chapter 10.1 part 2 - looping over the file object")
print()
filename = "learning_python.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
print()

print("This is chapter 10.1 part 3 - storing the lines in a list")
print()
filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.strip())
print()

print("This is chapter 10.2")
filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        modified_line = line.replace("python", "c")
        print(modified_line.strip())
print()

"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""
print("This is chapter 10.3")
print()
name = input("What is your name? ")

with open("guest.txt", "w") as file_object:
    person_name = file_object.write(name)
print()


print("This is chapter 10.4")
print()
with open("guest_book.txt", "a") as file_object:
    active = True
    while active:
        guest_name = input("Enter 'quit' to exit.\nPlease enter your name: ")
        
        if guest_name.lower() == "quit":
            active = False
        else:
            file_object.write(guest_name + "\n")
            print(f"Hello {guest_name.title()}")
print()

print("This is chapter 10.5")
print()
with open("poll_answers.txt", "a") as file_object:
    active = True
    while active:
        poll_response = input("enter 'quit' to exit.\nWhy do you like programming? ")
        
        if poll_response == "quit":
            active = False
        else:
            file_object.write(poll_response + "\n")
print()            
            
            
            
            
"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, youll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ )
and find a few texts youd like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>> line = "Row, row, row your boat"
>> line.count('row')
2
3
>> line.lower().count('row')
Notice that converting the string to lowercase using lower() catches
all appearances of the word youre looking for, regardless of how its
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.
"""

print("This is chapter 10.6")

try:
    num_1 = input("Enter one number: ")
    num_2 = input("Enter another number: ")
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = num_1 + num_2
except ValueError:
    print("You cannot add two strings") 
else:
    print(f"The sum total of {num_1} {num_2} is {total}.")


print()
print("This is chapter 10.7")

active = True
while active:
    try:
        num_1 = input("Enter 'q' to quit\nEnter one number: ")
        if num_1 == "q":
            print("You decided to quit the program")
            break
        num_2 = input("Enter 'q' to quit\nEnter another number: ")
        if num_2 == "q":
            print("You decided to quit the program")
            break

        num_1 = int(num_1)
        num_2 = int(num_2)
        total = num_1 + num_2
        
    except ValueError:
        print("You cannot add two strings") 
    else:
        print(f"The sum total of {num_1} {num_2} is {total}.")
        
print()
print("This is chapter 10.8")

"""Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.
"""

try:
    with open("cats.txt") as cat_object:
        cat_names = cat_object.readlines()
        
except FileNotFoundError:
    print("That file does not exist in the current directory.")

else:
    print("The following names in the cat file are: ")
    for i in cat_names:    
        print(f"- {i.strip()}")
    
print()
 
try:
    with open("dogs.txt") as dog_object:
        dog_names = dog_object.readlines()
        
except FileNotFoundError:
    print("That file does not exist in the current directory.")

else:
    print("The following names in the dog file are: ")
    for i in dog_names:    
        print(f"- {i.strip()}")
    
"""
It is good, but it couldve been cleaner if you made it a function.

def print_pet_names(filename, pet_type):
    try:
        with open(filename) as file_object:
            names = file_object.readlines()
    except FileNotFoundError:
        print(f"{filename} does not exist in the current directory.")
    else:
        print(f"The following names in the {pet_type} file are:")
        for name in names:
            print(f"- {name.strip()}")
    print()


print_pet_names("cats.txt", "cat")
print_pet_names("dogs.txt", "dog")
"""

print()
print("This is chapter 10.9 - moved dogs.txt file into chapter 10 sub folder")

def file_contents(filename, animal_type):
    try:
        with open(filename) as fileobject:
            animal_name = fileobject.readlines()
    except FileNotFoundError:
        pass
    else:
        print(f"The names of {animal_type} in the file {filename} are: ")
        for i in animal_name:
            print(f"- {i.strip()}")
        
file_contents("cats.txt", "cats")
file_contents("dogs.txt", "dogs")

print()
print("This is chapter 10.10")

try: 
    with open("money.txt") as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content.lower().count("the "))

print()

"""
10-11. Favorite Number: Write a program that prompts for the users favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! Its _____.”
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the users favorite number and store it in a
file. Run the program twice to see that it works.
10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the corr
"""
print("Chapter 10.11 - 10.13 are on a file")