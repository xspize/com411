def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    section_name = ""
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        section_name = parts[1].strip()
      else:
        if (section_name in data):        
          values = data[section_name]
          values.append(line.strip())
        else:
          data[section_name] = [line.strip()]

  print("Done!")
  return data

def run():
  data = search("data/files/txt/books.txt")

  with open("data/files/txt/generated.csv", "w") as file:
    for item in data.items():
      section = item[0]
      books = item[1]

      for book in books:
        file.write(f"{section},{book}\n")

run()
