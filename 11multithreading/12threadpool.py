#example of thread pool using ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
def task(n):
   return f"Task {n} done"
with ThreadPoolExecutor(max_workers=3) as executor:
   results = executor.map(task, range(5))
for r in results:
   print(r)


#submit()
def square(n):
   return n * n
with ThreadPoolExecutor(max_workers=2) as executor:
   future1 = executor.submit(square, 4)
   future2 = executor.submit(square, 5)
   print(future1.result())
   print(future2.result())


#complete function
from concurrent.futures import ThreadPoolExecutor, as_completed
def work(n):
   return n * 2
with ThreadPoolExecutor(max_workers=3) as executor:
   futures = [executor.submit(work, i) for i in range(5)]
   for future in as_completed(futures):
       print(future.result())

       