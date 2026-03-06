"""
Write a separate program to accomplish each of these exercises. Save each
program with a filename that follows standard Python conventions, using
lower case letters and underscores, such as simple_message.py and simple
_messages.py.

2-1. Simple Message: Assign a message to a variable, and then print that
message.

2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.
"""
print("This is chapter 2.1")
message = "This is a message"
print(message)
print()
print("This is chapter 2.2")
messageTwo = "This is another message"
print(messageTwo)
messageTwo = "Cancel that last message"
print(messageTwo)
print()
print()


"""
Save each of the following exercises as a separate file with a name like
name_cases.py. If you get stuck, take a break or see the suggestions in
Appendix C.

2-3. Personal Message: Use a variable to represent a persons name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”
2-4. Name Cases: Use a variable to represent a persons name, and then print
that persons name in lowercase, uppercase, and title case.
2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous persons name using a variable called famous_person. Then compose
your message and represent it with a new variable called message. Print your
message.
2-7. Stripping Names: Use a variable to represent a persons name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\ t" and "\ n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
"""
print("This is chapter 2.3")
personName = "Irem"
print(f"Hello {personName}, would you like to learn Python today?")
print()
print("This is chapter 2.4")
personNameTwo = "irem santos"
print(personNameTwo.upper())
print(personNameTwo.lower())
print(personNameTwo.title())
print()
print("This is chapter 2.5")
author = "oscar wilde" 
quote = "Be yourself, everyone else is already taken"
print(f"{author.title()} once said, '{quote}'.")
print()
print("This is chapter 2.6")
famous_person = "james dean"
famous_message = f"{famous_person} once said, 'Can I have fries with that?'"
print(famous_message)
print()
print("This is chapter 2.7")
herName = "  irem santos  "
print(herName)
print(f"\n{herName}")
print(herName.lstrip())
print(herName.rstrip())
print(herName.strip())
print()
print()

"""
2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once
on each line.
2-9. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.
"""
print("This is chapter 2.8")
print(4+4)
print(12-4)
print(4*2)
print(16/2)
print()
print("This is chapter 2.9")
favNum = 21
numMessage = f"My favorite number is {favNum}!"
print(numMessage)
print()
print()
"""
2-10. Adding Comments: Choose two of the programs youve written, and
add at least one comment to each. If you dont have anything specific to write
because your programs are too simple at this point, just add your name and
the current date at the top of each program file. Then write one sentence
describing what the program does.
"""
# Name: Toeside Funside
# Date: January 24, 2026
# This program prints a simple greeting message to the screen.
print("Hello world!")
print()
print()

