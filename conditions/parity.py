"""
x = int(input("What is x? "))

if x % 2 == 0:
    print("x is Even")
else:
    print("x is Odd")
"""

def main():
    x = int(input("What is x? "))

    if is_even(x):
        print("x is Even")
    else:
        print("x is Odd")

def is_even(n):
    # return True if n % 2 == 0 else False  # Alternative syntax
    # return n % 2 == 0  # Another alternative
    if n % 2 == 0:
        return True
    else:
        return False


main()

