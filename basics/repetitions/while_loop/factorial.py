#We wish to create a program to help Bop calculate the factorial of a specified number.
#The program should start by displaying the message "Please enter a number:".
print("Please enter a number:")
number = int(input())

#for the calculation
calculation = 0
# result
result = 1
#loop  to calculate the factorial for the specified number
while (calculation < number):
  calculation = calculation + 1
  result = result * calculation
#for showing the results
print ("The factorial is {}".format(result))
