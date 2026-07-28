import re

print("=== REGEX FULL DEMO ===\n")

# Sample text
text = "My phone number is 9876543210 and email is test@example.com"

# -------------------------------
# 1. BASIC PATTERNS
# -------------------------------
print("1. BASIC PATTERNS")

digits = re.findall(r"\d", text)
print("Digits:", digits)

words = re.findall(r"\w+", text)
print("Words:", words)

email = re.findall(r"\S+@\S+", text)
print("Email:", email)

print("\n-------------------------------\n")

# -------------------------------
# 2. MATCH vs SEARCH
# -------------------------------
print("2. MATCH vs SEARCH")

text2 = "Hello Python World"

match_result = re.match(r"Hello", text2)
if match_result:
    print("match(): Found at beginning ->", match_result.group())
else:
    print("match(): Not found")

search_result = re.search(r"Python", text2)
if search_result:
    print("search(): Found ->", search_result.group())
else:
    print("search(): Not found")

print("\n-------------------------------\n")

# -------------------------------
# 3. FINDALL & FINDITER
# -------------------------------
print("3. FINDALL & FINDITER")

text3 = "cat bat rat mat"

result = re.findall(r".at", text3)
print("findall():", result)

print("finditer():")
for match in re.finditer(r".at", text3):
    print(match.group(), "at position", match.start())

print("\n-------------------------------\n")

# -------------------------------
# 4. SUBSTITUTE & SPLIT
# -------------------------------
print("4. SUBSTITUTE & SPLIT")

text4 = "I love apples. Apples are tasty."

new_text = re.sub(r"apples", "oranges", text4, flags=re.IGNORECASE)
print("sub():", new_text)

split_text = re.split(r"\s", text4)
print("split():", split_text)

print("\n-------------------------------\n")

# -------------------------------
# 5. PRACTICAL EXTRACTION
# -------------------------------
print("5. PRACTICAL EXTRACTION")

text5 = "User: Ravi, Age: 21"

name = re.search(r"User:\s(\w+)", text5)
if name:
    print("Name:", name.group(1))

age = re.search(r"Age:\s(\d+)", text5)
if age:
    print("Age:", age.group(1))

print("\n-------------------------------\n")

# -------------------------------
# 6. EXTRA COMMON PATTERNS
# -------------------------------
print("6. EXTRA COMMON PATTERNS")

sample = "Contact: 9876543210, Email: demo@mail.com"

phone = re.search(r"\d{10}", sample)
if phone:
    print("Phone:", phone.group())

email2 = re.search(r"\S+@\S+", sample)
if email2:
    print("Email:", email2.group())

print("\n=== END OF DEMO ===")
