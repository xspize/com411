def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  select_direction = directions()

  for index in range(len(select_direction)):
      print("{}: {}.".format(index, select_direction[index]))

  user_input = int(input())
  return select_direction [user_input]

def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
   direction = menu()
   route.append(direction)
  print("Escape route: {}".format(route))


run()
