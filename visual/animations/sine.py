import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def animate(frame):
  global ax

  #The function should set the x limit for the axes to a minimum of 0 and a maximum of 720.
  ax.set_xlim(0, 720)
  #The function should then set the y limit for the axes to a minimum of -1 and a maximum of 1.
  ax.set_ylim(-1, 1)
  #The function should then create a NumPy array named x_values with a range from 0 to the current frame number.
  x_values = np.arange(0, frame)
  x_in_radians = x_values * (np.pi /180)
  #The function should then calculate the y values by multiplying the x values by PI/180
  y_values = np.sin(x_in_radians)

#Finally, the function should plot the points given by x and y.
  ax.plot(x_values,y_values)

def run():
  global fig
#The function should create an animation with 720 frames and an interval of 100.
  sine_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show()

run()
