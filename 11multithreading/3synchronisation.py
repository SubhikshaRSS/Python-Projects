#Using Lock
import threading
counter = 0
lock = threading.Lock()
def increment():
   global counter
   for _ in range(100000):
       lock.acquire()
       counter += 1
       lock.release()
threads = []
for _ in range(2):
   t = threading.Thread(target=increment)
   threads.append(t)
   t.start()
for t in threads:
   t.join()
print(counter)

#RLock -> lock = threading.RLock()
#SemaPhore
import threading
import time
sem = threading.Semaphore(2)
def task(name):
   with sem:
       print(f"{name} accessing resource")
       time.sleep(2)
for i in range(5):
   threading.Thread(target=task, args=(i,)).start()

#Event
import threading
event = threading.Event()
def waiter():
   print("Waiting...")
   event.wait()
   print("Done waiting!")
def setter():
   print("Setting event")
   event.set()
threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()

#Condition
import threading
condition = threading.Condition()
items = []
def producer():
   with condition:
       items.append(1)
       print("Produced")
       condition.notify()
def consumer():
   with condition:
       condition.wait()
       print("Consumed", items.pop())
threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()

#Barrier
import threading
barrier = threading.Barrier(3)
def task(n):
   print(f"Thread {n} waiting")
   barrier.wait()
   print(f"Thread {n} passed")
for i in range(3):
   threading.Thread(target=task, args=(i,)).start()