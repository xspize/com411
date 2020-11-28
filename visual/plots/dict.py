import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}
    print("What type of line would you like? :, -- or -")
    line = input()
    print("What colour? r, g or b?")
    colour = input()
    print("What style of marker would you like o,s or ^ ")
    marker = input()
    
    paths['line'] = line
    paths['colour'] = colour
    paths['marker'] = marker
    
    return paths

def generate():
    print("How many lines would you like to display?")
    
    lines = int(input())
    
    #The function should then create a loop that iterates as many times as the number of lines specified by user
    for number in range (lines):
        
        #Call the first function and store the result in a variable named values.
        values = data()
        
        #Display a line graph using the values stored in values and random values for x and y (see random.sample)
        x = rnd.sample(range(1,30),5)
        y = rnd.sample(range(1,30),5)
        
        #gets values from data()
        format = f"{values['colour']}{values['line']}{values['marker']}"
        
        plt.plot(x,y, format)
        plt.show()
        
def run():
    print("Running...")
    generate()
    print("Done!")
    
run()
