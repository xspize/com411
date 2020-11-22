import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}

  print("What kind of line would you like? :, -- or -?")
  line = input()
  print("What colour would you like? r, g or b?")
  colour = input()
  print("What style of marker would you like? o,s or ^")
  marker = input()

#The function should then store the line style, colour, marker style in the dictionary as key-value pairs
  paths['line'] = line
  paths['colour'] = colour
  paths['marker'] = marker

#return the dictionary
  return paths

def generate():
  print("How many lines would you like to display?")
  lines_display = int(input())


  for number in range(lines_display):
    values = data()

    x = rnd.sample(range(1,10),5)
    y = rnd.sample(range(1,10),5)

    format = f"{values['colour']}{values['line']}{values['marker']}"
    plt.plot(x, y, format)

  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")   


run()
