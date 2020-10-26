#The first function should be named likelihood and should have no parameters.
def likelihood():
#create a tuple and populate it with numbers
    likelihoods = (50, 38, 27, 99, 4)
#return those numbers
    return likelihoods
# declare function to store in a local variable the data from likelihood.
def run():
# stores data from another function into a local function
    local_likelihood = likelihood()
# prints the minimum number inside the tuple.
    print("Minimum likelihood of falling: {}%".format(min(local_likelihood)))
    
run()
    
