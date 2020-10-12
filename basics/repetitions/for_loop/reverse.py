#We wish to create a program that allows us to display a phrase in reverse.

#The program should begin by displaying the message What phrase do you see?

print("What phrase do you see?")
phrase = str(input())

print("\nReversing...The phrase is ", end="")
for reverse in range (len(phrase) -1, -1, -1):
  print(phrase[reverse],end="")
