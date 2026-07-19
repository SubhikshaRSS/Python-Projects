import mymath
result=mymath.add(10, 5)
print("Addition:", result)
result1=mymath.subtract(10, 5) 
print("Subtraction:", result1)    
result2=mymath.multiply(10, 5)
print("Multiplication:", result2)
result3=mymath.divide(10, 5)        
print("Division:", result3)
result4=mymath.square(6)
print("Square:", result4(6))
result5=mymath.numbersquare([1, 2, 3, 4, 5])
print("Numbers Square:", result5)
result6=mymath.sorting([("Arun", 25), ("Bala", 20), ("Chetan", 23)])
print("Sorted Objects:", result6)

import mypackage
print(mypackage.version)

from mypackage.module1 import add, subtract, multiply, divide, square, numbersquare, sorting
result7=add(15, 5)

import mypackage.module1 as m 
result8=m.add(20, 10)
print("Result 8:", result8)

import mymath as mm
result9=mm.add(30, 15)
print("Result 9:", result9)   

mm.calculate_area(5, 10)
print(__name__)
if __name__ == "__main__":
    print("Running as the main program")
else:
    print("Imported as a module")