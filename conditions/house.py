"""
name = input("What is your name? ")

if name == "Harry":
# if name == "Harry" or name == "Ron":  # Alternative syntax
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
elif name == "Ron":
    print("Gryffindor")
elif name == "Luna":
    print("Ravenclaw")
else:
    print("Who?")
"""

name = input("What is your name? ")


match name:
    case "Harry" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("Who?")
        