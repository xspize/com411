#We wish to create a program to help the robot communicate with Beep.

#The program should display the message "Please enter a phrase:"
print("Please enter a phrase:")
#The program should then read in the user's response.
user_input = input()
#The program should then display the word "Bop" repeatedly x number of times where x is the number of characters in the phrase entered by the user.
print(" Bop " * len(user_input))
