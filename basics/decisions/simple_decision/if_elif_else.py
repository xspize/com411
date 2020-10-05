##We wish to create a program that allows us to help Beep learn to paint.
##The program should start by prompting the user for a direction to move the paint brush (up, down, left or right).
##The program should then work out in which direction Beep should paint and display a suitable message.

print("Towards which direction should I paint (up, down, left or right)?")
user_input = input()
if (user_input == "up"):
    print("I am painting in the upward direction!")
elif(user_input == "down"):
    print("I am painting in the down direction!")
elif(user_input == "left"):
    print("I am painting in the left direction")
elif(user_input == "right"):
    print("I am painting in the right direction")
else:
    print("Sorry I don't know what you meant.")
