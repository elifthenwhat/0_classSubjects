"""
Try these short programs to get some firsthand experience with Pythons lists.
You might want to create a new folder for each chapters exercises to keep
them organized.
3-1. Names: Store the names of a few of your friends in a list called names. Print
each persons name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each persons name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
persons name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

print("This is chapter 3.1")
names = ["sam", "dave", "carol", "steve"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print()
print("This is chapter 3.2")
message = "Greetings "
messageTwo = "welcome to your new school."
print(f"{message}{names[0].title()},{messageTwo}")
print(f"{message}{names[1].title()},{messageTwo}")
print(f"{message}{names[2].title()},{messageTwo}")
print(f"{message}{names[3].title()},{messageTwo}")
print("This is chapter 3.3")
carBrands = ["honda", "toyota", "subaru"]
print(f"I would love to ride a {carBrands[0].title()} motorcycle.")
print(f"I would love to drive a {carBrands[1].title()} truck.")
print(f"{carBrands[2].title()} drivers are from Oregon.")
print()
print()

"""
The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people youd like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests cant make the
dinner, so you need to send out a new set of invitations. Youll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who cant make it.
• Modify your list, replacing the name of the guest who cant make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
42 Chapter 3
3-7. Shrinking Guest List: You just found out that your new dinner table wont
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know youre sorry you cant invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know theyre still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""
print("This is chapter 3.4")
dinnerGuests = ["irem", "silvia", "giada"]
print(f"{dinnerGuests[0].title()} you are invited to dinner.")
print(f"{dinnerGuests[1].title()} you are invited to dinner.")
print(f"{dinnerGuests[2].title()} you are invited to dinner.")
print()
print("This is chapter 3.5")
dinnerGuests = ["irem", "silvia", "giada"]
print(f"{dinnerGuests[0].title()} you are invited to dinner.")
print(f"{dinnerGuests[1].title()} you are invited to dinner.")
print(f"{dinnerGuests[2].title()} you are invited to dinner.") 
print(f"Aaaah! It looks like {dinnerGuests[2].title()} will not be able to join us.")
print()
dinnerGuests[2] = "samantha"
print(f"{dinnerGuests[0].title()} you are invited to dinner.")
print(f"{dinnerGuests[1].title()} you are invited to dinner.")
print(f"{dinnerGuests[2].title()} you are invited to dinner.") 
print()
print("This is chapter 3.6")
print("Good news, there is more room for more guests!")
dinnerGuests.insert(0, "karen")
dinnerGuests.insert(2, "sarah")
dinnerGuests.append("robin")
print(f"{dinnerGuests[0].title()} you are invited to dinner.")
print(f"{dinnerGuests[1].title()} you are invited to dinner.")
print(f"{dinnerGuests[2].title()} you are invited to dinner.") 
print(f"{dinnerGuests[3].title()} you are invited to dinner.")
print(f"{dinnerGuests[4].title()} you are invited to dinner.")
print(f"{dinnerGuests[5].title()} you are invited to dinner.") 
print()
print("This is chapter 3.6")
print("Sorry everyone, there is only two available seats left.")
poppedGuest = dinnerGuests.pop()
print(f"Sorry {poppedGuest.title()}, you are no longer invited.")
poppedGuest = dinnerGuests.pop()
print(f"Sorry {poppedGuest.title()}, you are no longer invited.")
poppedGuest = dinnerGuests.pop()
print(f"Sorry {poppedGuest.title()}, you are no longer invited.")
poppedGuest = dinnerGuests.pop()
print(f"Sorry {poppedGuest.title()}, you are no longer invited.")
print(f"The remaining people on the guest list is: {dinnerGuests}")
print()
print()
"""
3-8. Seeing the World: Think of at least five places in the world youd like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Dont worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
its back to its original order.
• Use sort() to change your list so its stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so its stored in reverse alphabetical order.
Print the list to show that its order has changed.
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else youd like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
"""
travelDestination = ["paris", "italy", "california", "thailand", "bali"]
print("This is the original list")
print(travelDestination)

print("This is a temporary sorted list.")
print(sorted(travelDestination))

print("This is the list in its original order")
print(travelDestination)

print("This is the original list reversed")
print(sorted(travelDestination,reverse=True))

print("This is the list in its original order")
print(travelDestination)

print("This is the list backwards")
travelDestination.reverse()
print(travelDestination)

print("This is the list in its original order")
travelDestination.reverse()
print(travelDestination)

print("This is the list sorted")
travelDestination.sort()
print(travelDestination)

print("This is the list reverse order")
travelDestination.sort(reverse=True)
print(travelDestination)
print()

print("This is chapter 3.9")
print(f"There will be a total of {len(dinnerGuests)} at tonight's dinner.")
print()

print("This is chapter 3.10")
sports = ["basketball", "soccer", "tennis", "swimming"]
print("This is the sports list")
print(sports)
print("This is a tempoary sorted list")
print(sorted(sports))
print("This is the list reversed")
sports.reverse()
print(sports)
print("This is the orignal list")
sports.reverse()
print(sports)