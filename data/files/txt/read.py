import os

#The first function should be named search and should take 1 parameter that represents a file name
def search(location):
  print("Searching...")
#The function should then open the specified file for reading.
  with open("data/files/txt/location.txt") as file:
#reads in between every single line of the file
    for line in file:
      print(f"Looked in {line}", end="")

  print("\n...Done!")

def run():
#function with file name as a parameter
  search("location.txt")

#runs the program
run()

