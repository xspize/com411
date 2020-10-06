##The program should start by prompting the user to enter a whole number.
##The program should then work out if the number is even or odd.
##Finally, the program should display a suitable message to indicate if the number is even or odd.

print("Please enter a whole number.")
number = int(input())
##checks if the number if even or odd
if (number % 2 != 0):
  print("The number " + str(number) + " is an odd number." )
else:
  print("The number " + str(number) + " is a even number.")

