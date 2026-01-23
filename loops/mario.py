"""
print("#")
print("#")
print("#")
"""

# for _ in range(3):
#     print("#")

def main():
    print_column()

def print_column():
    for _ in range(3):
        print("#")
# Alternatively ...
# def print_column(height):
#     print("#\n" * height, end="")

main()


def main():
    print_row()

def print_row(width):
    print("?" * width)

main()


def main():
    print_square()

def print_square(size):

    # for each row in square
    for i in range(size):
        
        # for each brick in row
        for j in range(size):
            print("#", end="")  # print brick without newline
        print()  # print newline after each row


main()

"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
"""
