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
  #The function should start by calling the first function with the file path and name visual/subplots/temps.txt and assign the resulting list of values to a local variable named data
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()


run()
