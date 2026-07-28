import re
text = "Hello 123"
result = re.search(r"\d+", text)
if result:
   print("Found:", result.group())

# re.search ->finds 1st match
s1=re.search("cat", "The cat is here")
print(s1.group())  # Output: cat

#re.findall() → Finds all matches
s2=re.findall(r"\d", "a1b2c3")
print(s2)  # Output: ['1', '2', '3']

#re.match() → Matches at start
s3=re.match("Hello", "Hello world")
if s3:
    print(s3.group())  # Output: Hello
else:
    print(s3)
#re.sub() → Replace text
s4=re.sub(r"\d", "#", "a1b2c3")
print(s4)  # Output: a#b#c#

# Email Pattern
import re
email = "test@@@example.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

#Match Funtion
day = 6
match day:
   case 1:
       print("Monday")
   case 2:
       print("Tuesday")
   case 3:
       print("Wednesday")
   case _:
       print("Invalid day")

#Multiple match function case
num = 5
match num:
   case 1 | 2 | 3:
       print("Between 1 and 3")
   case _:
       print("Other number")

#Using Conditions in Match Function
x = -1
match x:
   case x if x > 5:
       print("Greater than 5")
   case _:
       print("Less or equal to 5")

#Matching Sequences (List/Tuple)
data = (3,4)

match data:
   case (1, 2):
       print("Matched tuple")
   case _:
       print("No match")

#Match with Variables
point = (3, 4)

match point:
   case (x, y):
       print("X:", x, "Y:", y)

#Search Function
import re

text = "I have 50 apples"
result = re.search(r"\d", text)

if result:
   print("Found:", result.group())
#Access match details
import re

text = "Hello 123 world"
match = re.search(r"\d+", text)

if match:
   print(match.group())   # matched text
   print(match.start())   # start index
   print(match.end())     # end index

#Using Groups
import re

text = "Price: 500 USD"
match = re.search(r"(\d+)\sUSD", text)

if match:
   print(match.group())     # 500 USD
   print(match.group(0))   # 500 USD
   print(match.group(1))   # 500
   print(match.groups())    # ('500',)
#re.finditer()
import re

text = "cat bat rat"

for match in re.finditer("at", text):
   print(match.start())

