#import module os 
import os

def cwd():
#os.getcwd displays the file path of the current working folder
  path = os.getcwd()
  print(f"The current working folder is: {path}")
  print("The folder contains the following:")
#to display the content of this folder using the method listdir of the module
  for file in os.listdir(path):
    print(file)

#function to run the program
def run():
  print("Processing...")
  cwd()

#runs the program
run()
