#the first function should be named sum_weights and should have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the total weight.
def sum_weights(beep_weight, bop_weight):
  total_weight = beep_weight + bop_weight 
  return total_weight

#The second function should be named calc_avg_weight and should also have 2 parameters. The parameters represent the weight of each bot. The function should calculate and return the average weight of the bots. It should do this by calling the first function and using the return value.

def calculate_avg_weight(beep_weight, bop_weight):
  average = (beep_weight + bop_weight) / 2
  return average

#The third function should be named run and should have 0 parameters. The function should prompt the user to enter the weight for each bot. The function should then prompt the user to enter either the word "sum" or "average". If the user types in "sum" then this function should display the total age as given by the first function ( sum_weights"). Otherwise if the user types in "average" then this function should display the average weight as given by the second function ( calc_avg_weight).

def run():
  print("What is the weight of Beep?")
  beep_weight = float(input())
  print("What is the weight of Boop?")
  boop_weight = float(input())
  print("What would you like to calculate (sum or average)")
  action = input()

  if action == ("sum"):
    answer = sum_weights(beep_weight, boop_weight)
    print("The sum is {:.2f}".format (answer))
  elif action == ("average"):
    answer = calculate_avg_weight(beep_weight, boop_weight)
    print("The average is {:.2f}".format (answer))
  else:
    print("Action not recognized!")

#The program should also contain a single call to your run function at the end of your program that looks as follows:
#run the program
run()
