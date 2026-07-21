#writing and reading binary data using pickle module
import pickle
data = {"name": "Arun", "age": 20, "marks": [85, 90, 88]}

#Writing the data to a binary file using pickle
with open("data.pkl", "wb") as file:
   pickle.dump(data, file)

#Reading the pickled data:
with open("data.pkl", "rb") as file:
   data = pickle.load(file)
print(data)

#Writing multiple objects to a binary file using pickle
with open("multi.pkl", "wb") as file:
   pickle.dump([1, 2, 3], file)
   pickle.dump("Hello", file)
#Reading:
with open("multi.pkl", "rb") as file:
   print(pickle.load(file))
   print(pickle.load(file))