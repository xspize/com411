def short_pattern():
    pattern = {"sequence":"101","occurrences":5}
    return pattern

def medium_pattern():
    pattern = {"sequence":"111000","occurrences": 25}
    return pattern
    
def long_pattern():
    pattern = {"sequence":"1100110011001100","occurrences":50}
    return pattern
    
def run():
    print("Analysing patterns...")
#The function should then create a dictionary with the following key-value pairs:
    patterns = {
     "short sequence":short_pattern(),
     "medium sequence":medium_pattern(),
     "long sequence":long_pattern()       
    }
#Finally, the function should display the content of the dictionary as key-value pairs using an appropriate loop
    for key, value in patterns.items():
        print(f"{key}: {value}")

run()

#other way

def short_pattern():
  pattern = {}
  pattern["sequence"] = 101
  pattern["ocurrences"] = 5

  return pattern

def medium_pattern():
  pattern = {}
  pattern["sequence"] = 111000
  pattern["ocurrences"] = 25

  return pattern

def long_pattern():
  pattern = {}
  pattern["sequence"] = 1100110011001100
  pattern["ocurrences"] = 50

  return pattern

def run():
  print("Analysing patterns...") 
  value_pairs = {
  "Short sequence":short_pattern(),
  "Medium sequence":medium_pattern(),
  "Long sequence":long_pattern(),
  } 

  for key,value in value_pairs.items():
    print(f"{key}:{value}")

run()
