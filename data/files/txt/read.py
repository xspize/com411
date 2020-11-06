
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
#file_name is a condition inside the function that is later called in the run function.
def search(file_name):
  print("Searching...")
  #open file 
  with open(file_name) as file:
    #For each line in the file:
    for line in file:
      print(f"Looked in {line}",end="")
  print("\nDone!")


def run():
  #calls the text file
  search("data/files/txt/location.txt")



run()


