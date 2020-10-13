print("Program Started!")
print("Please enter an ASCII code:")
#user input
user_code = int(input())

if(user_code >= 32 and user_code <= 126):
ascii_letter = chr(user_code)
print("The character represented by the ASCII code {} is {}.".format(user_input, ascii_leter))
else:
  print("invalid number!")
  
 print("Program ended!")
