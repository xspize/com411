## Asking for the human name ##
print("What is your name human?")
human= input()
print("How old are you (in years)?")
age= int(input())
print("How tall are you (in meters)?")
height= float(input())
print("How much do you weigh (in kilograms)?")
weight= float(input())
##bmi calculation
bmi = weight / (height**2) 
##final print##
print("{} you are {}  years old and your bmi is {:.2f}.".format(human,age,bmi))