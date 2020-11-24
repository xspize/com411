import matplotlib.pyplot as plt
import csv

def read_data():
  
#The function should read the file visual/subplots/temps.csv and store its contents into a dictionary so that the dictionary contains the following key-value pairs:
#{
 #   'week1':[12, 14, 16, 15, 17, 16, 17],
 #   'week2':[18, 21, 20, 21, 23, 17, 16]
#}
  with open('visual/subplots/temps.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    header = next(csv_reader)
    data = {'week1':[], 'week2':[]}

    for line in csv_reader:
      data['week1'].append(float(line[0].strip()))
      data['week2'].append(float(line[1].strip()))
  
  return data

def run():
  #The function should start by calling the first function and storing the resulting dictionary in a local variable named data.
  data = read_data()
  
 #The function should then display the values using Matplotlib such that the resulting Figure consists of 2 subplots arranged vertically and sharing the same x-axis. 
# The first subplot should show a plot for week1 and the second subplot should show a plot for week 2.
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data['week1'])), data['week1'])
  ax2.plot(range(len(data['week2'])), data['week2'])
  plt.show()

 
run()
