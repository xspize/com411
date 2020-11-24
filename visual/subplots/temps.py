import matplotlib.pyplot as plt

def read_data(file_path):
  #creates empty list
  temps = []
  #opens file 
  with open(file_path) as file:
    #loops each line in file
    for line in file:
      #The function should then read each line in the file and store it into a list (remember to strip and int() or float()).
      temps.append(float(line.strip()))
      #the function should return the list of values.
  return temps

def run():
  #The function should start by calling the first function with the file path and name visual/subplots/temps.txt and assign the resulting list of values to a local variable named data.
  data = read_data('visual/subplots/temps.txt')
  #The function should then display the list of values named data in a Matplotlib graph consisting 
  #of two subplots placed horizontally.  The first subplot should show the data as a line graph and the second subplot should show the data as a bar chart.
  fig, (ax1, ax2) = plt.subplots(1, 2)
  #line graph
  ax1.plot(range(len(data)), data)
  #bar graph
  ax2.bar(range(len(data)), data)
  plt.show()


run()
