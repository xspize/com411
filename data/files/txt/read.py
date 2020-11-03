import os

def search(location):
  print("Searching...")
  with open("data/files/txt/location.txt") as file:
    for line in file:
      print(f"Looked in {line}")

    print("...Done!")

def run():
  search("location.txt")


run()

