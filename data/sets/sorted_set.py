#defines function
def observed():
# creates an empty list
    observations = []

#user input in the list
    for count in range (5):
        print("Please enter an observation:")
        user_input = input()
        observations.append(user_input)
    return observations
    
def remove_observations(observations):
    
    #checks if the loop is running
    is_running = True
    
    #loop to check if the user wants to remove more than one observation until he says no
    while(is_running):
        print("Do you wish to remove an observation? (yes/no)?")
        answer = input()
        
        if (answer == "yes"):
            print("What would you like to remove?")
            to_remove = input()
            observations.remove(to_remove)
# ends the loop if the user says no or something else than yes
        else:
            is_running = False
    
def run():
    observations = observed()
    remove_observations(observations)
    
    observations_set = set()
 #loop to check how many times the input was observed   
    for observation in observations:
        occurrences = observations.count(observation)
        observations_set.add( (observation, occurrences) )
# sorting the key and value in the variables observation and occurrences (observations_set)        
    for key, value in sorted(observations_set):
        print(f"{key} observed {value} times")
#runs the program        
run()
        
    
            
    
    
