#We wish to create a program that allows us to display a grid of ASCII emoji.
#The program should start by asking the user how many rows and columns they would like.
print("How many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

# Placing the row variable inside the first loop to make it repeat the same amount that the user inputs, then after, inside that loop, the loop will show the amount of columns desired by the user.
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-(", end="")
    print()
