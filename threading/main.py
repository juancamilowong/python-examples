import threading
import time
import random

def task(name):
    seconds = random.randint(1, 5);
    print(f"task {name} started {seconds} seconds")
    time.sleep(seconds)
    print(f"task {name} finished")

thread1 = threading.Thread(target=task, args=("Mountain",))
thread2 = threading.Thread(target=task, args=("Ocean",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()    