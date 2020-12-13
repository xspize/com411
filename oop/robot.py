class Robot:
    #class attribute:
    MAX_ENERGY = 100
    #instance attribute (init is the initilizer)
    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 0
    #instance  methods (create objects inside the class)
    def display(self):
        print(f"I am a {self.name}")

#if (__name__ == "__main__"):
# creates an object it can be named whatever I want
#it_can_be_any_name = Human()
#it_can_be_any_name.display_object()
Robot = Robot()
Robot.display()