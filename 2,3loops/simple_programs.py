#odd or even:
num=input("Enter a number:")
if int(num) % 2 == 0:   
    print("The number is even.")        
else:   
    print("The number is odd.")

num = input("Enter a number: ")
#tables:
for i in range(1, 6):
   print(num, "x", i, "=", int(num) * i)
#Factorial:
n=input("Enter a number:")
s=1
for k in range(1,int(n)+1):
 s=s*k
print("The factoial of",n,"is",s)

''' Take Multi Line command line input '''
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", a + b)



