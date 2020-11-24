import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
    
def animate(frame):   
  #The function should set the x limit of the axes to a minimum value of 0 and a maximum value of 10. 
  ax.set_xlim(0,10)
#The function should then set the y limit of the axes to a minimum value of 0 and a maximum value of 10.
  ax.set_ylim(0,10)
#Finally, the function should then plot a red circle marker with an x-value and a y-value equal to the current frame number.
  ax.plot(frame, frame, "ro")
     
def run():
  global fig  
  #The function should create an animation using FuncAnimation which calls the function animate, has 10 frames and an interval of 1000 milliseconds.
  simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  #the function should show the plot
  plt.show()

run()
