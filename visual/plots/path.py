import matplotlib.pyplot as plt

def coordinate():
  print("Please enter an x value:")
  x = int(input())
  
  print("Please enter a y value:")
  y = int(input())

  return (x,y)

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  #loop that iterates 4 times
  for count in range(4):
    data = coordinate()
    # Adds the first item of data (the x value) to x_values.
    x_values.append(data[0])
    # Adds the second item of data (the y value) to y_values.
    y_values.append(data[1])
  #return list
  return [x_values,y_values]

def run():
  #The function call the second function and store the result in variable named values.
  values = path()
  #The function should then display a line plot using values[0] for the x values and values[1] for the y values.
  #red dashed line with circle markers 
  plt.plot(values[0],values[1],'r--o')
  #contain suitable labels for the axes.
  plt.xlabel("x values")
  plt.ylabel("y values") 
  plt.show()


run()
