def search(file_name):
  print("Searching...", end ="")
  sections = []
  books = []

  with open(file_name) as file:
    for line in file:
      if line.startswith("Section:"):
        #separates the line from the others to display the right line that has sections in it, 
        section_name = line.split(":")[1]
        sections.append(section_name.strip())
        #.strip() is to remove \n's
      else:
        books.append(line.strip())

    print("Done!")
  #returns a tuple containing sections and books
  return (sections, books)

def save(file_name, data):
  print("Saving...", end ="")
  #open file to write in it
  with open(file_name,"w") as file:
    #write the line sections: to the file where [sections] is each section in data, the number [0] is for sections and [1] for books, because data is the value returned of sections,books
    file.write(f"Sections: {data[0]}\n")
    file.write(f"Books: {data[1]}\n")
  print("Done!")

def run():
  #store  search function in a local variable data 
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)

run()




