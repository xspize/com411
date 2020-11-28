import matplotlib.pyplot as plt


def read_data(file_path):
    #creates empty list
    values = []
    #opens file temps.txt
    with open('temps.txt') as file:
        #loops lines inside file
        for line in file:
            #adds values to empty list
            values.append(float(line.strip()))
    return values

def run():
    # inserts data from function inside local function
    data = read_data('temps.txt')
    
    #create subplots, fig is figure, ax1 and ax2 are both graphics, subplots(x,y) y creates 2 columns
    fig, (ax1,ax2) = plt.subplots(1, 2)
    
    #changes ax1 that is a plot
    ax1.plot(range(len(data)),data)
    
    #changes ax1 that is a bar
    ax2.bar(range(len(data)),data)
    
    plt.show()
    
#runs programn   
run()
