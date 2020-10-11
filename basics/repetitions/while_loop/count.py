#We wish to create a program that allows Beep to avoid live cables.
#The program should start by displaying the message "How many live cables must I avoid?".
print("How many live cables must I avoid?")
user_response = int(input())
#The program should then create a variable to track the number of live cables and set this to 0.
cable_count = 0
#he program should then use a while loop to do the following:
while (cable_count < user_response):
  print("\tAvoiding..", end="")
  cable_count = cable_count +1
  print("Done! " + str(cable_count) + " live cable avoided!")
  #Finally, the program should display the message "All live cables have been avoided."
else:
  print("")
  print("All live cables have been avoided.")
