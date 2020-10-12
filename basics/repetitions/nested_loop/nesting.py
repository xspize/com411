# Beep's program should first ask the user to enter a sequence of characters consisting of dashes and two markers e.g. "X----X".
print("Please enter a sequence:")
user_input = input()

print("Please enter the character for the marker:")
marker = input()


marker1 = -1
marker2 = -1

for position in range(0, len(user_input), 1):
    letter = user_input[position]

    if (letter == marker):
        if (marker1 == -1):
            marker1 = position
        else:
            marker2 = position


print("The distance between the markers is", marker2 - marker1 - 1)
