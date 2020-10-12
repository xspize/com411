#We wish to create a program that allows us to display a word character by character.

#The program should begin by displaying the message "What strange markings do you see?".

print("What strange markings do you see?")
user_response = input()

# basically followed the example above the exercise, took me  a while to figure out how to list the index 0 1 2 3, because the symbols were appearing instead but then I finally got it.
for markings in range (0,len(user_response),1):
  print("index",markings,":",user_response[markings])
