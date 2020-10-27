def observed():
    print("")
#creates a list
    observations = []
    
# Reads user input 7 times and adds the input to the list called observations
    for count in range (7):
        print("Please enter an observation:")
        user_input = input()
        observations.append(user_input)
    return observations
    
def run():
    print("Counting observations...")
    store_list = observed()
   
#The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list 
    observation_set = set()
    #loop reading the user input and shows the name and number of times the word was typed.
    for observation in store_list:
    # counts the amount of times the user input the names
        observation_set.add((observation, store_list.count(observation)))
        
    print(observation_set)
        
#runs the program
run()
    
    
