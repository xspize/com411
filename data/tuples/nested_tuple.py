def steps():
#create  list of tuples populated
    likelihoods = [ ("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4) ]
    return likelihoods
def run():
    return_list = steps()
    
#The function should then create two empty lists, good_steps and bad_steps.
    good_steps = []
    bad_steps = []

#The function should then loop through the list of steps retrieved previously and do the following for each step:
    for step in return_list:
        if(step[1] >= 50):
            bad_steps.append(step)
        else:
            good_steps.append(step)
    
#displays good steps and bad steps
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
    
#runs the program
run()

