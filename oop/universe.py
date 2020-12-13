from Planet import Planet
from robot import Robot
from human import Human
import random

class Universe:

#This class should contain an instance variable that represents a list of planets
    def __init__(self):
        self.planets = []

    def __repr__(self):
        return f"universe(planets={self.planets})"

    def __str__(self):
        return f"The universe contains {len(self.planets)} planets."

    #instance method
    def generate(self):
        #creates a planet
        planet = Planet()

        #adds a random number of humans and robots to the planet object

        for index in range(random.randint(1, 10)):
            robot = Robot(f"Robot{index}")
            planet.add_robot(robot)

        for index in range(random.randint(1, 10)):
            human = Human(f"Human{index}")
            planet.add_human(Human)

        # add to list of planets
        self.planets.append(planet)

if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()

  # You should add suitable code to test your code.
  print(repr(universe))
  print(universe)






