from inhabitant import Inhabitant

class Robot(Inhabitant):
    #class attribute:
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
    def __init__(self):
        super().__init__()
    #instance  methods (create objects inside the class)
    def display(self):
        print(f"I am a {self.name}")

# Magic methods

#The function repr returns a formal string representation of the object
    def __repr__(self):
        return f'Robot (name={self.name}, age={self.age}, energy={self.energy})'

#str returns an informal string representation of the object.
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'


if (__name__ == "__main__"):
# creates an object it can be named whatever I want
#it_can_be_any_name = Robot()
#it_can_be_any_name.display_object()
    robot = Robot()
#Robot.display()
#we can display the string returned by repr as follows:
    print(repr(robot))
#The function __str__ is called when attempt to display an object:
#print(Robot)
    robot.move(10)
    print(repr(robot))
    robot.eat(5)
    print(repr(robot))
    robot.eat(20)
    print(repr(robot))
