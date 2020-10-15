# displays the word in a box 
def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)

# displays the word in lower case 
def display_lower_case(word):
    print(word.lower())

# displays the word in upper case 
def display_upper_case(word):
    print(word.upper())

# displays the word mirrored
def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print("{} | {}".format(word, mirrored))
# repeats the word  in even and odd repetitions
def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        # odd repetition
        else:
            print(display_upper_case(word))
#definition to run the programs menu
def run():
    print("Please enter a word:")
    word = input()

    # remember the user has not yet selected an option
    response = 0

    while (response != 6):
        # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input()) 
 
        # determine and execute action
        if (response == 1):
            display_box(word)
        elif (response == 2):
            display_lower_case(word)
        elif (response == 3):
            display_upper_case(word)
        elif (response == 4):
            display_mirrored(word)
        elif (response == 5):
            display_repeated(word)
        elif (response == 6):
            break
        else:
            print("Unknown option.") 

run()
