import matplotlib.pyplot as plt


# marker styles can be specified using single characters
# these include o for circles, s for squares, ^ for triangle up, v for triangle down

#plt.plot(x, y, 'o')   # will display circle markers
#plt.plot(x, y, 's')   # will display square markers

# similarly, we can control the line styles
# these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines

#plt.plot(x, y, 'o-')  # will display circle markers with a solid line
#plt.plot(x, y, 'o--') # will display circle markers with a dashed line
#plt.plot(x, y, 'o:')  # will display circle markers with a dotted line

# colors can be specified using single characters where r is red, b is blue, g is green, etc.
# supported colours include red, blue, green, cyan, magenta, yellow, black and white.

#plt.plot(x, y, 'yo')   # will display yellow markers
#plt.plot(x, y, 'ro--') # will display a red dashed line

def small():
  x = [3, 3, 4, 4, 3]  # 3 in the end is to go back to the start
  y = [3, 4, 4, 3, 3]
  plt.plot(x,y,'r:o')

def medium():
  x = [2,2,5,5,2]
  y = [2,5,5,2,2]
  plt.plot(x,y,'g--s') #green dash line with square brakets

def large():
  x = [1,1,6,6,1]
  y = [1,6,6,1,1]
  plt.plot(x,y,'b-p') # lue solid line with pentagon markers 
   # only use plot after doing the other ones
def run():
  small()
  medium()
  large()
  plt.show()

run()
