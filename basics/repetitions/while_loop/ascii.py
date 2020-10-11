#We wish to create a program that allows Beep to avoid live cables.
#The program should start by displaying the message "How many bars should be charged?".
print("How many bars should be charged?")
#The program should then read in the user's response.
user_response = int(input())
#The program should then create a variable to track the number of bars charged and set this to 0.
bars_charged = 0
#The program should then use a while loop to do the following:
while (bars_charged < user_response):
  bars_charged = bars_charged +1
  print("Charging ", end="")
  print(" | "  * bars_charged)
else:
    print("")
    print("the battery is fully charged.")
