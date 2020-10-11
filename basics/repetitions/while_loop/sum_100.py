#We wish to create a program to help Bop calculate the sum of the first 100 numbers.

#The program should start by displaying the message "Calculating the sum of the first 100 numbers...".
print("Calculating the sum of the first 100 numbers...")
# this variable was set to sum the first 100 numbers after the loop.
calculate = 0
# the variable number is the variable used for the loop.
number = 0
while (number < 100):
  number = number + 1
  # by doing this it calculates the initial 100 numbers giving it a result of 5050.
  calculate = calculate + number
print("...Done the answer is ", calculate)
