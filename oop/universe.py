from Planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

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
            planet.add_human(human)

        # add to list of planets
        self.planets.append(planet)

#uses matplotlib to display the population (humans vs robots) for each planet.
    def show_populations(self):
        num_subplots = len(self.planets)

        fig, axs = plt.subplots(1, num_subplots)

        for index in range(num_subplots):
            planet = self.planets[index]
            num_humans = len(planet.inhabitants['humans'])
            num_robots = len(planet.inhabitants['robots'])

            if (num_subplots == 1):
                axs.bar([1, 2], [num_humans, num_robots])
            else:
                axs[index].bar([1, 2], [num_humans, num_robots])

    plt.tight_layout()
    plt.show()



if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.show_populations()
  # You should add suitable code to test your code.
  print(repr(universe))
  print(universe)






