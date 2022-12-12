from threading import Thread, Lock
import time 


database_val = 0

def increase(lock):
    with lock:
        global database_val
        local_val = database_val 

        
        local_val += 1
        time.sleep(0.1)  
        database_val = local_val
   

if __name__ == "__main__":
    lock = Lock()
    print(f"Start value {database_val}")
    thread1 = Thread(target=increase ,args=(lock,))
    thread2 = Thread(target=increase , args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"end value : { database_val}")

    print("Ended")