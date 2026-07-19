#pip install requests
import requests

response = requests.get("https://api.github.com")

print(response.status_code)

#pip install numpy
import numpy as np

numbers = np.array([10, 20, 30])

print(numbers)
print(numbers.mean())

#pip install pandas
import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Chetan"],
    "Age": [25, 20, 23]
}

df = pd.DataFrame(data)

print(df)

#pip install matplotlib
import matplotlib.pyplot as plt

marks = [70, 80, 90]

plt.plot(marks)
plt.show()