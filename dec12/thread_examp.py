from threading import Thread, Lock, current_thread
import time 
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f" we are in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":
    lock = Lock()
    q = Queue()
    num_thread = 10
    thread = Thread(target=worker, args=(q,lock))
    thread.daemon = True
    thread.start()
    

    for i in range(1,20):
        q.put(i)
    q.join()

    print('End of threads')
