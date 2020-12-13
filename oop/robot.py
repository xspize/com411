class Robot:
    #class attribute:
    MAX_ENERGY = 100
    laws = "Protect, Obey and Survive"

    # A static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

#- class methods: These are methods that are shared by all objects of the class and require an instance of the class.
# Class methods take cls (a reference to the class) as the first parameter.
#The can call other class methods and access class attributes but cannot access instance attributes.  They are often used to create an object of the class.
    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")


    #instance attribute (init is the initilizer)
    def __init__(self, name = "Bop", age = 1000):
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY
    #instance  methods (create objects inside the class)
    def display(self):
        print(f"I am a {self.name}")

#a method grow that increases the age of the object by 1
    def grow(self):
        self.age +=1

# a method eat that takes an amount as a parameter.  This should increase the energy of the object by the amount.  Note, energy should not exceed MAX_ENERGY.
    def eat(self, amount):
        potencial_energy = self.energy + amount
        if (potencial_energy > Robot.MAX_ENERGY):
            self.energy = Robot.MAX_ENERGY
            return potencial_energy - self.energy
        else:
            self.energy = potencial_energy
            return 0

#a method move that takes a distance as a parameter.  This should reduce the energy of the object by the distance. Note, energy should not fall below 0.
    def move(self, distance):
        potencial_energy = self.energy - distance
        if (potencial_energy < 0):
            self.energy = 0
            return self.energy - abs(potencial_energy)
        else:
            self.energy = potencial_energy
            return 0

# Magic methods

#The function repr returns a formal string representation of the object
    def __repr__(self):
        return f'Robot (name={self.name}, age={self.age}, energy={self.energy})'

#str returns an informal string representation of the object.
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'


#if (__name__ == "__main__"):
# creates an object it can be named whatever I want
#it_can_be_any_name = Human()
#it_can_be_any_name.display_object()
Robot = Robot()
#human.display()
#we can display the string returned by repr as follows:
print(repr(Robot))
#The function __str__ is called when attempt to display an object:
#print(human)
Robot.move(10)
print(repr(Robot))
Robot.eat(5)
print(repr(Robot))
Robot.eat(20)
print(repr(Robot))
