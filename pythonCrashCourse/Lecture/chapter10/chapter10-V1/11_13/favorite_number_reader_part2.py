import json

# Load the favorite number if it has not been stored previously 
# Otherwise, prompt for the username and store it 

filename = "favorite_number_part2.json"

try:
    with open(filename) as f:
        fav_num = json.load(f)
        print(f"I know your favorite number! Its {fav_num}")

except FileNotFoundError:
    fav_num = input("Please enter your favorite number: ")
    
    filename = "favorite_number_part2.json"
    with open(filename, "w") as f:
        json.dump(fav_num, f)
        print(f"I will remember your favorite number {fav_num} when you come back")
