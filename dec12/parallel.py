from multiprocessing import Process
import os
import time

def sqr ():
    for i in range(100):
        i * i
        time.sleep(0.1)
        


processes = []
num_processes = os.cpu_count()


for i in range(num_processes):
    P = Process(target=sqr)
    processes.append(P)


for P in processes:
    P.start()

for P in processes:
    P.join()

print('End all processes')