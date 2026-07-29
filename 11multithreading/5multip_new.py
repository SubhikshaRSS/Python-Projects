#passing arguments
from multiprocessing import Process
def square(n):
   print(n * n)
p = Process(target=square, args=(5,))
p.start()
p.join()

#Multi process
from multiprocessing import Process
def worker(n):
   print(f"Process {n}")
processes = []
for i in range(3):
   p = Process(target=worker, args=(i,))
   processes.append(p)
   p.start()
for p in processes:
   p.join()

#Using pool
#Multi process runs automatically
from multiprocessing import Pool
def square(n):
   return n * n
if __name__ == "__main__":
   with Pool(3) as p:
       results = p.map(square, [1, 2, 3, 4, 5])
       print(results)

#Sharing data process using queue
from multiprocessing import Process, Queue
def worker(q):
   q.put("Hello")
q = Queue()
p = Process(target=worker, args=(q,))
p.start()
p.join()
print(q.get())

# Value/Array usage
from multiprocessing import Value
counter = Value('i', 0)  # shared integer