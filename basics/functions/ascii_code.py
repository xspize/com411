print("Program Started!")
print("Please enter a standard character:")
letter = str(input())

if len(letter) == 1:
  print("The ASCII code for {} is {}".format(letter,ord(letter)))
  
print("program ended!")
