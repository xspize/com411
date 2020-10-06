##Beep is learning about mathematical operators. Beep wishes to understand comparison operators by being able to identify the smallest of two numbers.

print("Please enter the first number.")
first_number = int(input())
print("Please enter the second number.")
second_number = int(input())
if (str(first_number) < str(second_number)):
  print("The first number is the smallest!")
if (str(second_number) < str(first_number)):
  print("The second number is the smallest!")
elif (str(first_number) == str(second_number)):
  print("Both numbers are equal.")

  
