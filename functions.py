import math
print(math.sqrt(16))   # Square root → 4.0
print(math.factorial(5))  # 120
print(math.pi)  # 3.14159...

import random
print(random.randint(1, 10))  # Random number between 1 and 10
print(random.choice([1, 2, 3]))  # Random selection

import datetime
today = datetime.date.today() #.now,.year,.month,.day can also be used
print(today)

#import entire package
import math
print(math.sqrt(25))

# import Specific Function
from math import sqrt
print(sqrt(36))

#import alias name
import math as m
print(m.pi)