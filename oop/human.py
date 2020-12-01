#creates a class
class Robot:
    
    #A class atribute
    laws = "Protect, Obey and Survive"
    
    # A class method
    def the_laws(self):
        print(Robot.laws)
        
    #an initialiser (special instance method)
    def __init__(self):
        
        #An Instance attribute
        self.name = "Robot"
        self.age = 0
        
    # An instance method
    def display(self):
        print(f"I am a {self.name}")
        

if (__name__ == "__main__"):
    
#creates object
  robot = Robot()
  robot.display()
  robot.the_laws()
  
class Human:
    
    #Class attribute
    MAX_ENERGY = 100
    
    #initialiser
    def __init__(self):
        
        #instance attribute
        self.name = "Human"
        self.age =  0
        self.energy = Human.MAX_ENERGY
        
    #instance method
    def display(self):
        print(f"I am  {self.name} and have {self.energy} energy.")
        
# object
if (__name__ == "__main__"):
  human = Human()
  human.display()
        
    
    
