#We wish to create a program that allows us to display a phrase in reverse.
#The program should begin by displaying the message "What phrase do you see?".
print("What phrase do you see?")
user_response = input()

print("\t Reversing...")

reversed = ""

for number in user_response:
  reversed = number + reversed

print(reversed)


