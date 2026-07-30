for i in range(10):
   if i == 5:                #break
       break
   print(i)

for i in range(5):
   if i == 2:
       continue              #continue
   print(i)

for i in range(3):
   pass                     #pass
                              
x = 10
if x > 5:
   print("Greater than 5")      #if

x = 3
if x % 2 == 0:
   print("Even")           #if-else
else:
   print("Odd")

marks = 75
if marks >= 90:
   print("A Grade")
elif marks >= 60:          #elif
   print("B Grade")
else:
   print("C Grade")

for i in range(3):
   for j in range(2):        #Nested Loops
       print(i, j)


for i in range(3):           #for and else
   print(i)
else:
   print("Loop finished")


# Print even numbers from 1 to 10   example
for i in range(1, 11):
   if i % 2 == 0:
       print(i)