#creates function
def pattern():
#creates a dictionary populated with words and numbers
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
#returns the directionary
    return sequences
    
#runs the program    
def run():
#transfer the other function to an inside function
    local_sequences = pattern()
#prints the dictionary out
    print(local_sequences)
    
#runs the program
run()
    
