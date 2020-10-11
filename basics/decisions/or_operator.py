
#The program should start by asking the user to enter the type of adventure.
print("What type of adventure should I have?")
user_input = input()
#If the type of adventure is "scary" or "short" then the program should display the message "Entering the dark forest!".
if ((user_input == "scary") or (user_input == "short")):
  print("Entering the dark forest!")
##If the type of adventure is "safe" or "long" then the program should display the message "Taking the safe route!".
elif ((user_input == "safe") or (user_input == "long")):
      print("Entering the safe route!")
##Otherwise, in all other cases, the message "Not sure which route to take." should be displayed.
else:
        print("Not sure which route to take.")
