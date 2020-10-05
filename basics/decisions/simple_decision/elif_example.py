##Note how the elif is used to check a related condition and provide an alternative and mutually exclusive path.

##Let us consider another example:

print("What are you?")

entity = input()

if (entity == "Human"):
    print("You are a human!")
elif (entity == "Robot"):
    print("You are a robot!")
elif (entity == "Animal"):
    print("You are an animal!")
else:
    print("I do not know what you are!")

print("Analysis complete.")

##Together, if…elif…else allow us to implement decisions in our code which can be used to solve more sophisticated problems.