class Human:
    #class attribute:
    MAX_ENERGY = 100
    #instance attribute (init is the initilizer)
    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY
    #instance  methods (create objects inside the class)
    def display(self):
        print(f"I am {self.name}")

#if (__name__ == "__main__"):
# creates an object it can be named whatever I want
#it_can_be_any_name = Human()
#it_can_be_any_name.display_object()
human = Human()
human.display()