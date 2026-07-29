
#example for multiprocessing
from multiprocessing import Pool, Process
def task():
   print("Process running")

def square(n):
    print(n*n)
    return n*n  

def worker(n):
    print(f"Process {n}")
    
from multiprocess import Process, Queue
def f(q):
    q.put("hello world")
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get()) # Output: hello world
    p.join()
    p1 = Process(target=task)
    p1.start()   # start process
    p1.join()    # wait for completion

#multiprocessing with arguments
    p2 = Process(target=square, args=(5,))
    p2.start()
    p2.join()

#multiple multiprocessing
    processes = []
    for i in range(3):
        p3 = Process(target=worker, args=(i,))
        processes.append(p3)
        p3.start()
    for p3 in processes:
        p3.join()

#using pool
    with Pool(3) as p4:
       results = p4.map(square, [1, 2, 3, 4, 5])
       print(results)
