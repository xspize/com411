##The program should start by asking the user to enter the cover type (hard or soft) of the book.
##If the book has a "soft" cover then the program should ask the user if the book is "perfect bound".
##If the answer is "yes" then the message "Soft cover, perfect bound books are very popular!" should be displayed
##otherwise the message "Soft covers with coils or stitches are great for short books" should be displayed.
##Alternatively, if the book has a "hard" cover then the message "Books with hard covers can be more expensive!" should be displayed.##

print("What type of cover does the book have?")
cover = input()

if (cover == "soft"):
    print("Is the the book perfect bound?")
    bound = input()

    if (bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

else:
      print("Books with hard covers can be more expensive!")
