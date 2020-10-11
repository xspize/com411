#We wish to create a program that allows Beep to remove the cables holding the robot.

#The program should start by displaying the message "How many cables should I remove?".
print("How many cables should I remove?")
#The program should then read in the user's response.
cables = int(input())
#The program should then create a variable to track the number of removed cables and set this to 0.
cables_count = 0
#The program should then use a while loop to do the following:
while (cables_count < cables):
cables_count = cables_count + 1
# Display the message "Removed cable."
print("Removed cable.",cables_count)

