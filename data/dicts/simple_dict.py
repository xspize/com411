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
    
    
# Another way to do it:

def pattern():
  sequences = {}
  sequences["Long Sequence"] = 1
  sequences["Medium Sequence"] = 2
  sequences["Short Sequence"] = 3

  return sequences

def run():
  print(pattern())


run()

