#creates a class
class Robot:
    
    #A class atribute
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100
    
    # A class method
    def the_laws(self):
        print(Robot.laws)

    def grow(self):
        self.age +=1
    
        
    #an initialiser (special instance method)
    def __init__(self):
        
        #An Instance attribute
        self.name = "Robot"
        self.age = 100
        self.eat = 30
        self.move = 40
        self.energy = Robot.MAX_ENERGY
        self.eat = 10 + Robot.MAX_ENERGY
        self.move = Robot.MAX_ENERGY - 40
        
    #repr returns a formal string representation of the object  
    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'
        
    # An instance method
    def display(self):
        print(f"I am a {self.name}")
        

if (__name__ == "__main__"):
    
#creates object
  robot = Robot()
  robot.display()
  robot.the_laws()
  #necessary to show the repr
  print(robot)
  
class Human:
    
    #Class attribute
    MAX_ENERGY = 100
    
    #initialiser
    def __init__(self, name, age):
        
        #instance attribute
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY
        self.eat = 10 + Human.MAX_ENERGY
        self.move = Human.MAX_ENERGY - 40
        
    def grow(self):
        self.age  +=1
     
    #str returns an informal string representation of the object   

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'
        
    #instance method
    def display(self):
        print(f"I am  {self.name} and I ate a burger which increased my energy to {self.eat} and then I started running and wasted {self.move} energy.")
        
        
# object
if (__name__ == "__main__"):
  Joao = Human("João", 23)
  Joao.display()
  Joao.grow()

  #necessary to show the str or repr
  print(Joao)
  
        
    
    
