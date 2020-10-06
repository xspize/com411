##The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally, the program should display the number of even numbers and odd numbers entered.

print("Please enter the first whole number.")
first_number = int(input())
print("Please enter the second whole number.")
second_number = int(input())
print("Please enter the third whole number.")
third_number = int(input())

odd = 0
even = 0

if (first_number % 2 != 0):
  even = even + 1  
else:
  odd = odd +1

if (second_number % 2 != 0):
  even = even + 1 
else:
  odd = odd +1

if (third_number % 2 != 0):
  even = even + 1
else:
  odd = odd +1

print("There were "  + str(even) + " and " + str(odd) + " odd numbers.")
