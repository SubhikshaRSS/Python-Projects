
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

print("=== COLLECTIONS, NAMEDTUPLE & DICT DEMO ===\n")

# -------------------------------
# 1. DICTIONARY BASICS
# -------------------------------
print("1. DICTIONARY")

student = {
    "name": "Ravi",
    "age": 21,
    "course": "Python"
}

print("Dictionary:", student)

# Access
print("Name:", student["name"])

# Add / Update
student["age"] = 22
student["grade"] = "A"

print("Updated dict:", student)

# Loop
for key, value in student.items():
    print(key, ":", value)

print("\n-------------------------------\n")

# -------------------------------
# 2. COUNTER
# -------------------------------
print("2. COUNTER")

text = "banana"
count = Counter(text)

print("Counter:", count)
print("Most common:", count.most_common(2))

print("\n-------------------------------\n")

# -------------------------------
# 3. DEFAULTDICT
# -------------------------------
print("3. DEFAULTDICT")

d = defaultdict(int)

d["a"] += 1
d["b"] += 2

print("defaultdict:", dict(d))

# Example: grouping
words = ["leg", "hen","log","box", "bat", "ball","cat", "car", "dog", "dot","mat","sat","pin","tin","bun","fun","run","sun"]

group = defaultdict(list)
print(group)
for word in words:
    print("Grouping word:", word)
    print(word[1], "->", group[word[1]])
    group[word[1]].append(word)
    print(group)
print("Grouped:", dict(group))

print("\n-------------------------------\n")

# -------------------------------
# 4. ORDEREDDICT
# -------------------------------
print("4. ORDEREDDICT")

od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3

print("OrderedDict:", od)

print("\n-------------------------------\n")

# -------------------------------
# 5. DEQUE
# -------------------------------
print("5. DEQUE")

dq = deque([1, 2, 3])

dq.append(4)        # add right
dq.appendleft(0)    # add left

print("Deque:", dq)

dq.pop()            # remove right
dq.popleft()        # remove left

print("After pop:", dq)

print("\n-------------------------------\n")

# -------------------------------
# 6. NAMEDTUPLE
# -------------------------------
print("6. NAMEDTUPLE")

Student = namedtuple("Student", ["name", "age", "course"])

s1 = Student("Ravi", 21, "Python")

print("NamedTuple:", s1)
print("Name:", s1.name)
print("Age:", s1.age)

print("\n-------------------------------\n")

# -------------------------------
# 7. DICT COMPREHENSION
# -------------------------------
print("7. DICT COMPREHENSION")

numbers = [1, 2, 3, 4]

square_dict = {x: x**2 for x in numbers}
print("Squares:", square_dict)

print("\n-------------------------------\n")

# -------------------------------
# 8. MERGING DICTS
# -------------------------------
print("8. MERGING DICTS")

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1, **d2}
print("Merged dict:", merged)

print("\n=== END OF DEMO ===")
