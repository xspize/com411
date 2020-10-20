# defining directions
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# creates function with a loop for directions
def menu():
  print("Please select a direction.")
  direction = directions()

  for index in range(len(direction)):
    print("{}: {}.".format(index, direction[index]))

# runs the function menu

def run():
  menu()

# runs the program
run()
