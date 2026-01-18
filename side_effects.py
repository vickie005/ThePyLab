emoticon = "v.v"   # sad face

def main():
    global emoticon
    say("Is anyone there?") 
    emoticon = "^-^"   # happy face
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()
