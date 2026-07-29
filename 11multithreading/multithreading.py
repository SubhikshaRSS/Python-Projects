#example of multithreading with lock
import threading
lock = threading.Lock()
counter = 0

def increment():
   global counter
   for _ in range(1000):
       with lock:
           counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
   t.start()

for t in threads:
   t.join()

print(counter)

# example of multithreading without lock
def print_numbers():
   for i in range(5):
       print(i)

def print_letters():
   for ch in ['A', 'B', 'C', 'D']:
       print(ch)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
print("Multithreading without lock started.")
print("Thread 1 is alive:", t1.is_alive())
print("Thread 2 is alive:", t2.is_alive())
t1.join()
t2.join()
print("Multithreading without lock completed.")