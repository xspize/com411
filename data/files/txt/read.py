
# Approach 1: using read

def search(file_name):
  print("Searching...")
#The function should then open the specified file for reading.
  with open(file_name) as file:
    lines = file.read().split('\n')
    for line in lines:
      print(f"Looked in {line}.")
    print("..Done!")


def run():
  search("data/files/txt/location.txt")


run()

# Approach 2: without using read

def search(file_name):
  print("Searching...")
  with open(file_name) as file:
    for line in file:
      print(f"Looked in {line[:-1]}.")

  print("...Done!")


def run():
  search("data/files/txt/location.txt")

run()

