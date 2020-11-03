
def search(file_name):
  print("Searching...")
  sections = []
  books = []

  with open(file_name) as file:
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        sections.append(parts[1].replace('\n',''))
      else:
        books.append(line.replace('\n',''))

  print("Done!")

#return lists as a tuple (it can be a return)
  return (sections, books)

def save(file_name, data):
  print("Saving...")
  with open(file_name, "w") as file:
    file.write("Sections: ")
    for index in range(len(data[0])):
      if (index < len(data[0])  - 1):
        file.write(f"{data[0][index]},")
      else:
        file.write(f"{data[0][index]}")

    file.write("\nBooks:")
    for book in data[1]:
      file.write(f"{book},")

  print("Done!")

def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)


run()


