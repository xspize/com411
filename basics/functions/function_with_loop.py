#def function
def cross_bridge(distance):
  for step in range(distance):
    print("Crossed step.")

  if (distance > 5):
    print("the bridge is collapsing!")
  else:
    print("We must keep going!")


#use function
cross_bridge(3)
cross_bridge(6)

