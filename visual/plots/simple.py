#import global function to use plot
import matplotlib.pyplot as plt

#The first function should be named display and should take 2 parameters.
#The first parameter is a list of x values.
#The second parameter is a list of y values.
def display(xvalues,yvalues):
  #The function should display a line plot using the arguments supplied for the parameters.
    plt.plot(xvalues, yvalues)
    plt.show()
  
def run():
  # create lists with values
  x_values = [1,2,3,4,5]
  y_values = [1,4,9,16,25]
  #The function should then call the first  function passing x_values and y_values as arguments.
  display(x_values,y_values)

#runs the function
run()
