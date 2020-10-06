##The program should start by displaying the message "Where should I look?"
print("Where Should I look?")
##The program should then read the user's response
response = input()

if (response == "in the bedroom"):
  print("Where in the bedroom should I look?")
  under_bed = input()
  if (under_bed == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery.")

elif(response == "in the bathroom"):
    print("Where in the bathroom should I look?")
    baththub = input()
  
    if (baththub == "in the bathtub"):
      print("Found a rubber duck but no battery")
    else:
      print("Found a wet surface but no battery.")

elif(response == "in the lab"):
  print("Where in the lab should I look?")
  table = input()

  if (table == "on the table"):
      print("Yes! I found my battery!")
  else:
    print("Found a wet surface but no battery.")


else:
  print("I do not know where that is but I will keep looking.")
