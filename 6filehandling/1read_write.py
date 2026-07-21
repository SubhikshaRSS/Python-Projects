#Reading a file
file = open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/example.txt", "r")  # "r" means read mode
content = file.read()
print(content)

#Reading a file line by line
for line in file:
   print(line)
file.close()

#Overwrites -w
file = open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/example.txt", "w")  # "w" means write mode
file.write("Hello heyy world!")
file.close()

# appending a file -a
file = open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/example.txt", "a")
file.write("\nThis is an appended line.\nSubhiksha")
file.close()

#Automatically closing a file using 'with' statement
with open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/example.txt", "r+") as file:
    content = file.read()
    file.write("\nThis line is added using 'with' statement.")
print(content)