from inhabitant import Inhabitant

class Human(Inhabitant):
    #class attribute:
    #MAX_ENERGY = 100
    #instance attribute (init is the initilizer)
    def __init__(self, name="Human", age=0):
        super().__init__(name, age)
        #instance variables

# Magic Methods

#The function repr returns a formal string representation of the object
    def __repr__(self):
        return f'Human (name={self.name}, age={self.age}, energy={self.energy})'

#str returns an informal string representation of the object.
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    #instance  methods (create objects inside the class)
    def display(self):
        print(f"I am {self.name}")

#if (__name__ == "__main__"):
# creates an object it can be named whatever I want
#it_can_be_any_name = Human()
#it_can_be_any_name.display_object()
   # human = Human()
#human.display()
#we can display the string returned by repr as follows:
  #  print(repr(human))
#The function __str__ is called when attempt to display an object:
#print(human)
  #  human.move(10)
   # print(repr(human))
    #human.eat(5)
    #print(repr(human))
    #human.eat(20)
    #print(repr(human))

if (__name__ == "__main__"):
  # create an object of type Human
  human = Human()

  # display the current state of the object
  print(repr(human))

  # invoke the method move on the object
  human.move(10)

  # display the current state of the object
  print(repr(human))

  human.eat(2)

  print(repr(human))
