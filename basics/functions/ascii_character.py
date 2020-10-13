print("Program Started!")
print("Please enter an ASCII code:")
#user input
user_code = int(input())

#Check that the number is in the range 32 - 126 
range1 = 32
range2 = 126

# the number in within the range then the program should
#determine the ASCII character from the number using the built-in function chr().
if user_code in range (range1, range2):
  letter = chr(user_code)
  #display the message
  print("The character represented by the ASCII code {} is {}".format(user_code, letter))
else:
  print("error")
  #end message
print("Program ended.")
