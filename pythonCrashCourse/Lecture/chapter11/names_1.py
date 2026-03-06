from name_function_0 import get_formatted_name

print("Enter 'q' anytimde to quit: ")

while True:
    first = input("\nPlease enter your first name: ")
    if first == "q":
        break
    last = input("\nPlease enter your last name: ")
    if last == "q":
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")

