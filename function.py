def hello(to="world"): # the 'world ' after 'to' is default incase the user doesn't input any name.
    print("Hello,", to)


hello()
name = input("What's your name? ")
hello(name)

"""
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main() # calling whichever function you want to run
"""
def main():
    print ("Hello, world")
    print("Python is fun!")

main()
