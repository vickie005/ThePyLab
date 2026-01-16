# Ask user for their name
name = input("What is your name? ") # .strip().title()

# Remove leading/trailing whitespace
name = name.strip()

"""
Capitalize the user's name...
name = name.capitalize()
"""

# capitalize the first letter of each word
name = name.title()

"""
Remove trailing space and capitalize the name...
name = name.strip().title()"""

# say hello to the user
# print("Hello, " + name + "!")
print(f"Hello, {name}!")

# split the name into the first and last name...
#first, last = name.split(" ")
#print(f"Hello, {first} !")

