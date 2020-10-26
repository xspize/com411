def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    #Finally, the function should find and return the minimum and maximum values in a tuple.
    return min(likelihoods), max(likelihoods)

def run():
    #local variable calling function
    falling = likelihood()
    #prints returned values from function likelihood
    print(f"Minimum likelihood of falling: {falling[0]}%")
    print(f"Maximum likelihood of falling: {falling[1]}%")  

#runs the function
run()


    
