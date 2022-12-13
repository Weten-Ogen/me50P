from multiprocessing import Process,Lock, Queue

import os
import time

def square(numbers, queue, lock):
    for i in numbers:
        queue.put(i + 1)

def make_neg(numbers,queue, lock):
    for i in numbers:
        with lock:
            queue.put(-1 * i)


        
        


if __name__ == "__main__":
   lock = Lock()
   numbers = range(1,6)
   q = Queue()
   q1 = Process(target=square, args=(numbers,q,lock))
   q2 = Process(target=make_neg, args=(numbers,q, lock))

   q1.start()
   q2.start()

   q1.join()
   q2.join()

   while not q.empty():
       print(q.get())      