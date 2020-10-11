#We wish to create a program that allows us to display some mountains.
#The program should begin by displaying the message "How many mountains should I display?"
print("How many mountains should I display?")
mountains = input()

##using function for to show the amount of mountains the user wants
for count in range (int(mountains)):
    print("           __")
    print("          /  \_")
    print("         /^    \ ")
    print("        /  ^    \_ ")
    print("      _/ ^ ^     ^\ ")
    print("     /  ^     ^    \ ")



#empty print to give space
print("")
print("Done!")
