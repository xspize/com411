##We wish to create a program that demonstrates the following functionality:

##- Decisions with if...elif...else statements
##- Nested decisions
##- Multiple conditions with logical (AND, OR and NOT) operators

##Initial question
print("I just woke up and feel dizzy.")
print("Should I see a doctor or call mom?")
#program reading user response
user_input = input()

# Decisions using if/elif/else
if (user_input == "go to doctor"):
  print("Ok! I just need to find my umbrella first to go outside thought..")
  print("Where can I find one?")
  kitchen = input()
  if (kitchen == "kitchen"):
    print("Okay I got the umbrella! let's go outside then!")
    print()
    print("I can't seem to find the hospital.. should I turn right or left?")
    user_decision = input()
# Condition using not operator
    if not (user_decision == "right"):
        print("Noooo! It's the wrong way...")
    else:
        print("ooray! I found the hospital! time to go inside and talk to the doctor!")
        print()
        print("Doctor: Hello young boy what's wrong?")
        sick = input()
        print("Doctor: Okay... understandable.. do you have other synthoms?")
        sick2 = input()
        # Condition using and operator
        if ((sick == "headache") and (sick2 == "no")):
          print("Here, take this medicine, you'll eventually feel better.")

elif (user_input == "call mom"):
  print("Mom! come downstairs please my head hurts!")
  print("")
  print("Mom: What's wrong son?")
  print("My head feels dizzy.")
  print("What should Beep's mom do to make him feel better?")
  mom_decision = input()
  #condition using or operator
  if ((mom_decision == "call doctor") or (mom_decision == "get medicine")):
      print("Sorry son.. I have to go to work now so there's not much that I can do..")
      print("Do you want me to call your dad?")
      call_dad = input()
  if (call_dad == "yes"):
      print("Ok I'll call him right away.")
      print("Phone Conversation: Beep is sick! come home right now!")
      print("Beep's Dad: I'm on my way!")
      print("Just wait for your dad son, alright?")
      wait = input()
      if ((wait == "ok mom")):
        print("Good boy. You'll eventually feel better.")
      else:
        print("NO! I DON'T WANT TO WAIT FOR DAD, I'LL GO TO THE DOCTOR MYSELF!")

    
