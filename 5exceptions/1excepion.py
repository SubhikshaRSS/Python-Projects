#try-finally Exceptions:
try:
   file = open("data.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("File not found")
finally:
   if 'file' in locals():
       file.close()
   print("File closed")

# Handling Specific Exceptions
try:
   num = int(input("Enter a number: "))
   result = 10 / num
except ZeroDivisionError:
   print("Cannot divide by zero")
except ValueError:
   print("Invalid input")
else:
   print("Result:", result)
try:
   x = 10 / 2
except:
   print("Error")
else:
   print("No error, result:", x)

# Using args in exceptions
try:
   x = int("abc")
except ValueError as e:
   print(e.args)

   #Multiple args , Raise an exception
try:
   raise Exception("Error occurred", 404)
except Exception as e:
   print(e.args)

#Access Individual arguments
try:
   raise Exception("File not found", 404)
except Exception as e:
   print("Message:", e.args[0])
   print("Code:", e.args[1])

#Multi exception in one line
try:
   x = int("abc")
except (ValueError, TypeError):
   print("Error occurred")

# Re Raising same exception
try:
   x = 10 / 0
except ZeroDivisionError:
   print("Handling error")
   try:
      raise Exception("Error display o test")   # re-raises the exception
   except Exception as e:
      print("Caught exception:", e)