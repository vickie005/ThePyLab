"""
i = 3
while i != 0:
    print("Meow!")
    i -= 1 # i = i - 1
"""

# i = 0
# while i < 3:
#     print("Meow!")
#     i += 1  # i = i + 1



for i in range(3): #for i in [0, 1, 2]: 
    print("Meow!")

# print("Meow!\n" * 3)  # prints "Meow!" 3 times with new lines in between


while True:
    n = int(input("What is n?   "))
    if n > 0:
        break   
for _ in range(n):
    print("Meow!")

# Functions
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow!")

main()


