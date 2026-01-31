WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to spelling bee!")
    print("Your letters are: A, I, P, C, R, H, G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").strip().upper() #word eg. hair, chair, pair

    #TODO: Check if guess in dictionary
    if guess in WORDS.keys():
        print(f"Good job! You scored {WORDS[guess]} points.")

print("That's the game!")


main()

