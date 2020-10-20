# The first function should be named directions and should have no parameters.
def directions():
  #The function should populate the list with the following items: "Move Forward", "Move Backward", "Turn Left" and "Turn Right". 
  directions = ["Move forward","Move backward","Turn Left","Turn right"]
  return directions
 

def run():
  print(directions())

run()