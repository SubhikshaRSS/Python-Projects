#Search & Replace

#Replaces all occurrences of a substring
text = "Hello World Hello World Hello World"
new_text = text.replace("World", "Python")
print(new_text)

#Replace limited occurences
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2)
print(new_text)

#Pattern based replacement (Advanced method)
import re
text = "My number is 12345"
new_text = re.sub(r"\d+", "XXXXX", text)
print(new_text)

#Case insensitive replace
import re
text = "Hello hello HELLO"
new_text = re.sub(r"hello", "hi", text, flags=re.IGNORECASE)
print(new_text)

#Replace Using Function
import re
def double(match):
   return str(int(match.group()) * 2)
text = "Values: 10 20 30"
result = re.sub(r"\d+", double, text)
print(result)

#Removing unwanted characters
import re
text = "Hello@# World!!"
clean = re.sub(r"[^a-zA-Z0-9 ]", "", text)
print(clean)

# Replace email domain
text = "user@gmail.com"
print(text.replace("gmail.com", "yahoo.com"))

# Mask phone number
import re
text = "9876543210"
print(re.sub(r"\d{6}$", "******", text))

#=================Extended Reg Exp========================

# Capturing & Grouping
import re
text = "Price: 500 USD"
match = re.search(r"(\d+)\sUSD", text)
if match:
   print(match.group(1))  # 500

#Named Groups
import re
text = "Date: 2026-04-20"
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
if match:
   print(match.group("year"))   # 2026

#Non Capturing Groups
n=re.search(r"(?:Mr|Mrs)\. Smith", "Mr. Smith")
print(n.group())  # Mr. Smith

#LookAhead Future check
import re
text = "100USD"
match = re.search(r"\d+(?=USD)", text)
if match:
   print(match.group())  # 100
# (?=...) = positive lookahead

#LookBehind Past check
match = re.search(r"(?<=USD)\d+", "USD100")
if match:
   print(match.group())  # 100

#Negative Look Ahead
n1=re.search(r"\d+(?!USD)", "100EUR")
print(n1.group())  # 100
# Matches digits not followed by “USD”
 
#Flag modifiers
import re
text = "hello"
n2=re.search("HELLO", text, re.IGNORECASE)
print(n2.group())  # hello

#re.IGNORECASE → case-insensitive
#re.MULTILINE → multi-line matching
#re.DOTALL → . matches newline

#Verbose mode (Easier way to read patterns)
pattern = r"""
\d{4}   # Year
-       # Separator
\d{2}   # Month
-       # Separator
\d{2}   # Day
"""
re.search(pattern, "2026-04-20", re.VERBOSE)

#Combining patterns
re.findall(r"(cat|dog|bird)", "I have a cat and a dog")

####################Wild Card ##################
#Match Single Char
import re
text = "cat bat rat"
result = re.findall(r".at", text)
print(result)
#['cat', 'bat', 'rat']

#Match multiple char
# .* → match any number of characters
text = "hello world"
match = re.search(r"h.*d", text)
print(match.group())
# Output:  hello world

#Greedy (default)
re.search(r"<.*>", "<h1>Title</h1>")
#Matches: <h1>Title</h1>

#Non-greedy (.*?)
re.search(r"<.*?>", "<h1>Title</h1>")
# Matches: <h1>
# ? makes it match the shortest possible string

#Other wild card patterns
re.findall(r"[cr]at", "cat rat bat")
re.findall(r"\d", "a1b2c3")

#Match literal dot
re.search(r"\.", "file.txt")

re.search(r"a.*b", "a\nb")  # No match 

#Use re.DOTALL:
re.search(r"a.*b", "a\nb", re.DOTALL)