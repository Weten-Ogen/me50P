from threading import Thread
import os
import time

def sqr():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_thread = 10

for i in range(num_thread):
    t = Thread(target=sqr)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end of threads')