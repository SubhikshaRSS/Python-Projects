# Writing binary data to a file
with open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/data.bin", "wb") as file:
   file.write((25).to_bytes(1, 'big'))   # age
   file.write((500).to_bytes(2, 'big'))  # score

#Reading it back:
with open("D://_ASubhiksha/coding/python/Python-Projects/6filehandling/data.bin", "rb") as file:
   age = int.from_bytes(file.read(1), 'big')
   score = int.from_bytes(file.read(2), 'big')
print(age, score)