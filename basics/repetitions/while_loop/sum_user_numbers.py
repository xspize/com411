#We wish to create a program to help Bop retrieve some numbers and calculate their sum.
#The program should start by displaying the message "How many numbers should I sum up?".
print("How many numbers should I sum up?")
#The program should then retrieve the user's response.
numbers = int(input())
# amount is set to 0 because it will be used inside the while function to give the user a prompt to choose between given numbers
amount = 0
# calculation is for the user input once the numbers that should be summed up are added to the program
calculation = 0

while (amount < numbers):
  amount = amount + 1
  print("Enter number {} of {}".format(amount,numbers))
  calculation = calculation + int(input())
  
#prints the answer, tip for myself: tabs are very important, I was having an issue that it kept showing up along "enter number x of x because the print function wasn't positioned well"  
print("The answer is {}".format(calculation))
