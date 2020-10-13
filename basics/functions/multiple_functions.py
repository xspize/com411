def display_ladder(steps):

  print("|  |")
  #This function should display an ASCII ladder with the same number of steps as the value of the parameter steps.
  for step in range(steps):
    print("****")
    print("|  |")

#The second function should be named create_ladder and should have no parameters.  This function should ask the user for the number of steps and then use the value in a call to the first function.
def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

#Finally, the program should contain a call to the second function
create_ladder()
