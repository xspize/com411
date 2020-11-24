import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  ax.cla()
  #The function should set the x limit for the axes to a minimum of 0 and a maximum of 720.
  ax.set_xlim(0, np.pi)
  #The function should then set the y limit for the axes to a minimum of -1 and a maximum of 1.
  ax.set_ylim(-1, 1)
  x_values = np.arange(0, 2*np.pi)
  y_values = np.sin(x_values + frame / 50)

#Finally, the function should plot the points given by x and y.
  ax.plot(x_values,y_values, 'b')

def run():
  
#The function should create an animation with 720 frames and an interval of 100.
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()

run()
