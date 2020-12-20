class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
      self.name = name
      self.age = age
      self.energy = self.MAX_ENERGY

  def grow(self):
        self.age += 1

 # a method eat that takes an amount as a parameter.  This should increase the energy of the object by the amount.  Note, energy should not exceed MAX_ENERGY.
  def eat(self, amount):
        potencial_energy = self.energy + amount
        if (potencial_energy > self.MAX_ENERGY):
            self.energy = self.MAX_ENERGY
            return potencial_energy - self.energy
        else:
            self.energy = potencial_energy
            return 0

# a method move that takes a distance as a parameter.  This should reduce the energy of the object by the distance. Note, energy should not fall below 0.
  def move(self, distance):
        potencial_energy = self.energy - distance
        if (potencial_energy < 0):
            self.energy = 0
            return self.energy - abs(potencial_energy)
        else:
            self.energy = potencial_energy
            return 0