def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b    
def square(a):
    return lambda a:a*a

def numbersquare(numbers):
    return list(map(lambda x: x**2, numbers))

def sorting(objects):
    objects.sort(key=lambda x: x[1])


def calculate_area(length, width):
    area = length * width
    if __name__ == "__main__":
        print("Running as the main program")
    else:
        print("Imported as a module")
    print(__name__)
    return area