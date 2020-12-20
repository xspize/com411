from robot import Robot
from human import Human

class Planet:

#The class should contain the following instance variables:
 # humans - a list of human objects (initially an empty list)
 # robots - a list of robot objects (initially an empty list)

#Replace the list of humans and the list of robots with a single dictionary named inhabitants which is an instance attribute.  Initially, the dictionary should looks as follows
    def __init__(self):
        self.inhabitants = []

    # magic methods

# __repr__ - returns a string containing a formal representation of a planet object (includes the list of humans and the list of robots)
    def __repr__(self):
        return f"planet(inhabitants={self.inhabitants})"

#   __str__ - return a string containing an informal representation of a planet object (includes the list of humans and the list of robots)

    def __str__(self):
        return f"This planet has {len(self.inhabitants)} inhabitants."

    # instance methods


    def add(self, inhabitant):
        self.inhabitants.append(inhabitant)


    def remove(self, inhabitant):
        self.inhabitants.remove(inhabitant)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  prins = Human("Prins")
  planet.add(prins)
  print(repr(planet))
  print(planet)


