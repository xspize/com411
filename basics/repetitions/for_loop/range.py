#We wish to create a program that adjusts the light level of Beep and Bop's night vision.

#The program should begin by displaying the message What level of brightness is required?
print ("What level of brightness is required?")
even_number = int(input())

print("\nAdjusting brightness...\n")

#using the for range with a variable created in it,  followed by a print of * symbols.
for odd_number in range(2, even_number + 1, 2):
    print("Beep's brightness level:", "*" * odd_number)
    print("Bop's brightness level:", "*" * odd_number)
