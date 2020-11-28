import matplotlib.pyplot as plt

def coordinate():
    print("Enter an x value:")
    # read in the user's response and store it in a variable named x.
    x = int(input())
    print("Enter an y value:")
    # read in the user's response and store it in a variable named y.
    y = int(input())

    # return a tuple containing x and y.
    return (x,y)

def path():
    print("Retrieving path...")
    
    #creates empty list for x_values and y_values
    x_values = []
    y_values = []
    
    #loop that iterates 4 times
    for count in range(4):
        
        #Calls the first function and stores the result in a variable named data.
        data = coordinate()
        
        #Adds the first item of data (the x value) to x_values.
        x_values.append(data[0])
        #Adds the second item of data (the y value) to y_values.
        y_values.append(data[1])
        
    #return a list containing x_values and y_values.    
    return [x_values,y_values]

def run():
    
    #calls the second function and store the result in variable named value
    values = path()
    
    #display a line plot using values[0] for the x values and values[1] for the y values.
    #The line plot should draw a red dashed line with circle markers
    plt.plot(values[0],values[1], 'r--o')
    
    # contain suitable labels for the axes.
    plt.xlabel("x values")
    plt.ylabel("y values")
    
    #shows the graph
    plt.show()
    
    
run()
    
    
