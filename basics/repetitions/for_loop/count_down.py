#We wish to create a program that counts down the distance (in number of steps) to the cave.

#The program should begin by displaying the message "How far are we from the cave?".

print("How far are we from the cave?")
steps = int(input())

for count in range (steps, 0, -1):
  print(count,"steps remaining.")

print("We have reached the end of the cave!")

#note to myself: range(start,stop,step) example: (steps(variable) is the number introduced by the user, 0 is when it should stop, and -1 is the  countdown, if it was -2 for example it would count differently.)


