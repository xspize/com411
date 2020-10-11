
##The program should start by displaying the message "What did I hear?"
print("What did I hear?")
##The program should then read the user's response
user_input1 = input()
##The program should then display the message "What did I see?"
print("What did I see?")
user_input2 = input()
##If the user entered "grrr" and "two red eyes" then program should display the message "There is a scary creature. I should get out of here!".
if ((user_input1 == "grrr") and (user_input2 == "two red eyes")):
  print("There is a scary creature. I should get out of here!")
## Otherwise the program should display the message "I am a little scared but I will continue."
else:
    print("I am a little scared but I will continue.")

